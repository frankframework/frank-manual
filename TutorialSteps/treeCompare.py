# This file compares two directories for TutorialSteps without
# accessing the file system. This is done by an instance of class
# TreeComparison. That class receives the relevant file names
# and their contents from the outside world. It also receives from
# the outside world the list of expected differences. These
# differences are encoded as FileDifference objects.
#
# Class TreeComparison does not access the file system.
# This makes it easy to write extensive unit tests that
# you can find in file testTreeCompare.py.

from .stringListCompare import checkNonNegativeInt
from .stringListCompare import checkNonEmptyStringList
from .stringListCompare import Comparison
from .stringListCompare import ExpectedUpdate
from .stringListCompare import HighlightedWindow
from .stringListCompare import comparatorIndentInsensitive
from .stringListCompare import comparatorIndentSensitive
from .stringListCompare import sortedByFirst
from .rst import makeRst
from .rst import makeMarkdown

class GeneratedSnippet:
    def __init__(self, name, linesRst, linesMd):
        if not type(name) is str:
            raise TypeError("Snippet name should be a string")
        checkNonEmptyStringList(linesRst)
        checkNonEmptyStringList(linesMd)
        self._name = name
        self._linesRst = linesRst
        self._linesMd = linesMd
    def getName(self):
        return self._name
    def getLinesRst(self):
        return self._linesRst
    def getLinesMd(self):
        return self._linesMd

class Snippet:
    def __init__(self, name):
        if not type(name) is str:
            raise TypeError("Snippet name should be string")
        self._snippetName = name
        self._numLinesBefore = 0
        self._numLinesAfter = 0
        self._markupLanguage = "none"
    def getSnippetName(self):
        return self._snippetName
    def setNumBefore(self, numContext):
        checkNonNegativeInt(numContext)
        self._numLinesBefore = numContext
    def setNumAfter(self, numContext):
        checkNonNegativeInt(numContext)
        self._numLinesAfter = numContext
    def setMarkupLanguage(self, markupLanguage):
        if not type(markupLanguage) is str:
            raise TypeError("markupLanguage should be str")
        self._markupLanguage = markupLanguage
    def apply(self, windowList):
        if not type(windowList) is list:
            raise TypeError("Expected a list, elements should be HighlightedWindow")
        if not all([isinstance(w, HighlightedWindow) for w in windowList]):
            raise TypeError("Expected all list elements to be HighlightedWindow")
        if len(windowList) == 0:
            raise ValueError("Expected at least one Window")
        for w in windowList:
            w.prepend(self._numLinesBefore)
            w.append(self._numLinesAfter)
        joinResult = windowList[0]
        for w in windowList[1:]:
            if not joinResult.hasOverlap(w):
                return None, None, "Modifications to combine in this snippet do not touch"
            joinResult = joinResult.join(w)
        linesRst, error = makeRst(joinResult, self._markupLanguage)
        if error is not None:
            return None, joinResult, error
        linesMarkdown, error = makeMarkdown(joinResult, self._markupLanguage)
        if error is not None:
            return None, joinResult, error
        result = None
        if (linesRst is not None) and (linesMarkdown is not None):
            result = GeneratedSnippet(self._snippetName, linesRst, linesMarkdown)
        return result, joinResult, error

# We want to compare relative paths. We do not want
# confusion over Windows or Linux path separators.
# Therefore we request the user to provide a class
# as string list.
class RelPath:
    def __init__(self, components):
        checkNonEmptyStringList(components)
        self._asString = "/".join(components)
    def __str__(self):
        return self._asString

class Change:
    def __init__(self, numOld, numNew, doHighlight, snippet):
        checkNonNegativeInt(numOld)
        checkNonNegativeInt(numNew)
        if not type(doHighlight) is bool:
            raise TypeError("doHighlight should be bool")
        if not isinstance(snippet, Snippet):
            raise TypeError("Snippet expected")
        if (numNew == 0) and (doHighlight):
            raise ArithmeticError("Cannot highlight in snippet when all lines are removed")
        self._numOld = numOld
        self._numNew = numNew
        self._doHighlight = doHighlight
        self._snippet = snippet
    def getSnippet(self):
        return self._snippet
    def getSnippetName(self):
        return self._snippet.getSnippetName()
    def isHighlighted(self):
        return self._doHighlight
    def toExpectedUpdate(self):
        return ExpectedUpdate(self._numOld, self._numNew)

class FileDifference(object):
    def __init__(self, relPath):
        if not isinstance(relPath, RelPath):
            raise TypeError("RelPath expected")
        self._relFileName = str(relPath)
    def getRelFileName(self):
        return self._relFileName
    def getWrittenSnippetNames(self):
        return set([])
    def applyTo(self, oldLines, newLines):
        if oldLines is not None:
            checkNonEmptyStringList(oldLines)
        if newLines is not None:
            checkNonEmptyStringList(newLines)
        return self._applyToUnchecked(oldLines, newLines)
    def _applyToUnchecked(self, oldLines, newLines):
        return None, None

class FileAddDifference(FileDifference):
    def __init__(self, relPath):
        super(FileAddDifference, self).__init__(relPath)
    def _applyToUnchecked(self, oldLines, newLines):
        if oldLines is not None:
            return None, "Expected that file is added, but file is already in old directory"
        if newLines is None:
            return None, "Expected that file is added, but file is not in new directory"
        return None, None

class FileDeleteDifference(FileDifference):
    def __init__(self, relPath):
        super(FileDeleteDifference, self).__init__(relPath)
    def _applyToUnchecked(self, oldLines, newLines):
        if oldLines is None:
            return None, "Expected that file is deleted, but it is not present in old directory"
        if newLines is not None:
            return None, "Expected that file is deleted, but it is present in new directory"
        return None, None

class FileModifyDifference(FileDifference):
    def __init__(self, relPath):
        super(FileModifyDifference, self).__init__(relPath)
        self._changes = []
    def addChange(self, change):
        if not isinstance(change, Change):
            raise TypeError("Change expected")
        self._changes.append(change)
    def getWrittenSnippetNames(self):
        return {c.getSnippetName() for c in self._changes}
    def _applyToUnchecked(self, oldLines, newLines):
        if oldLines is None or newLines is None:
            return None, "Modification expected, but file is not present in old or new directory"
        expectedUpdates = [c.toExpectedUpdate() for c in self._changes]
        comparison = Comparison(oldLines, newLines, expectedUpdates, comparatorIndentInsensitive)
        comparison.compare()
        if comparison.hasComparisonError():
            return None, comparison.getComparisonError()
        windows = comparison.getWindows()
        self._applyRequestedHighlights(windows)
        snippetNames = self.getWrittenSnippetNames()
        snippetsByName, error = self._getSnippetsByName()
        if error is not None:
            return None, error
        result = []
        editRegions = []
        for snippetName in snippetNames:
            snippetWindows = [windows[i] for i in range(0, len(windows)) if self._changes[i].getSnippetName() == snippetName]
            snippet, editRegion, error = snippetsByName[snippetName].apply(snippetWindows)
            if error is not None:
                return None, error
            result.append(snippet)
            editRegions.append(editRegion)
        error = self._checkEditRegionsOfDifferentSnippetsDontOverlap(editRegions)
        if error is not None:
            return None, error
        return result, None
    def _applyRequestedHighlights(self, windows):
        for i in range(0, len(self._changes)):
            if self._changes[i].isHighlighted():
                windows[i].highlightAll()
    def _getSnippetsByName(self):
        result = dict()
        for c in self._changes:
            key = c.getSnippetName()
            if key in result:
                if result[key] != c.getSnippet():
                    return None, "Duplicate definition of snippet {0}".format(key)
            else:
                result[key] = c.getSnippet()
        return result, None
    def _checkEditRegionsOfDifferentSnippetsDontOverlap(self, editRegions):
        erl = sortedByFirst(editRegions)
        if len(erl) <= 1:
            return None
        else:
            noOverlap = all([not erl[i-1].hasOverlap(erl[i]) for i in range(1, len(erl))])
            if noOverlap:
                return None
            else:
                return "The snippets generated from this file are not independent"

class TreeCompareItem:
    def __init__(self, relPath):
        if not isinstance(relPath, RelPath):
            raise TypeError("RelPath expected")
        self._relPath = str(relPath)
        self._oldLines = None
        self._newLines = None
        self._expected = None
    def setOld(self, lines):
        checkNonEmptyStringList(lines)
        self._oldLines = lines
    def setNew(self, lines):
        checkNonEmptyStringList(lines)
        self._newLines = lines
    def setExpected(self, fd):
        if not isinstance(fd, FileDifference):
            raise TypeError("FileDifference expected")
        self._expected = fd
    def run(self):
        if self._expected is None:
            error = self._checkEqual()
            return None, error
        snippets, error = self._expected.applyTo(self._oldLines, self._newLines)
        if error is not None:
            error = "File {0}: ".format(self._relPath) + error
        return snippets, error
    def _checkEqual(self):
        if self._oldLines is None or self._newLines is None:
            return "File {0}: Unexpectedly added or removed".format(self._relPath)
        comparison = Comparison(self._oldLines, self._newLines, [], comparatorIndentSensitive)
        comparison.compare()
        if comparison.hasComparisonError():
            return comparison.getComparisonError()
        else:
            return None

class TreeComparison:
    def __init__(self, fileDifferences):
        if not type(fileDifferences) is list:
            raise TypeError("List expected. It should contain FileDifference instances")
        if not all([isinstance(d, FileDifference) for d in fileDifferences]):
            raise TypeError("Every item of the list should be a FileDifference")
        self._fileDifferences = fileDifferences
        self._items = dict()
    def addOld(self, relPath, lines):
        key = self._commonAddLines(relPath, lines)
        self._items[key].setOld(lines)
    def addNew(self, relPath, lines):
        key = self._commonAddLines(relPath, lines)
        self._items[key].setNew(lines)
    def _commonAddLines(self, relPath, lines):
        if not isinstance(relPath, RelPath):
            raise TypeError("RelPath expected")
        checkNonEmptyStringList(lines)
        key = str(relPath)
        if not key in self._items:
            self._items[key] = TreeCompareItem(relPath)
        return key
    def run(self):
        errors = self._mapDifferencesToItems()
        if len(errors) >= 1:
            return None, errors
        errors = self._checkNoDuplicateSnippets()
        if len(errors) >= 1:
            return None, errors
        errors = []
        snippets = []
        for item in list(self._items.values()):
            itemSnippets, error = item.run()
            if error is not None:
                errors.append(error)
            if itemSnippets is not None:
                snippets.extend(itemSnippets)
        if len(errors) == 0:
            errors = None
        return snippets, errors
    def _mapDifferencesToItems(self):
        pathsOfActualFileDiffs = set(self._items.keys())
        pathsOfExpectedFileDiffs = set([d.getRelFileName() for d in self._fileDifferences])
        pathsOnlyExpected = pathsOfExpectedFileDiffs - pathsOfActualFileDiffs
        errors = ["Expected update not matched about file: {0}".format(p) for p in pathsOnlyExpected]
        if len(errors) >= 1:
            return errors
        for fd in self._fileDifferences:
            key = fd.getRelFileName()
            self._items[key].setExpected(fd)
        return []
    def _checkNoDuplicateSnippets(self):
        existingSnippets = set([])
        errors = []
        for fd in self._fileDifferences:
            names = fd.getWrittenSnippetNames()
            duplicates = names & existingSnippets
            for d in duplicates:
                errors.append("Duplicate definition of snippet {0}".format(d))
            existingSnippets = existingSnippets | names
        return errors

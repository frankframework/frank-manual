# Used by treeCompare.py to compare the contents of two files.
# For each file, the contents is provided as a list of strings.
# Each of these strings represents one line in a file.

comparatorIndentInsensitive = lambda first, second: first.strip() == second.strip()
comparatorIndentSensitive = lambda first, second: first == second

def checkNonEmptyStringList(stringList):
    if not type(stringList) is list:
        raise TypeError("Not a list: " + str(stringList))
    if not all([type(line) is str for line in str(stringList)]):
        raise TypeError("List should contain only strings: " + str(stringList))
    if len(stringList) == 0:
        raise ValueError("String list should contain at least one line")

def checkNonNegativeInt(i):
    if not type(i) is int:
        raise TypeError("Should be int")
    if i < 0:
        raise ValueError("Should not be negative")

def getIndentAndCheck(line):
    if not type(line) is str:
        raise TypeError("line should be string")
    if len(line) == 0:
        return None, None
    numIndent = 0
    for c in line:
        if c == " ":
            numIndent += 1
        elif c == "\t":
            err = "Line contains tabs: " + line
            return 0, err
        elif c == "\r":
            err = "Line contains \\r: " + line
            return 0, err
        elif c == "\n":
            err = "Line contains \\n: " + line
            return 0, err
        else:
            return numIndent, None

def unindentAndCheck(lines):
    checkNonEmptyStringList(lines)
    lineIndents = []
    for line in lines:
        indent, err = getIndentAndCheck(line)
        if err is not None:
            return None, err
        if indent is not None:
            lineIndents.append(indent)
    minIndent = min(lineIndents)
    return [line[minIndent:] for line in lines], None

class ExpectedUpdate:
    def __init__(self, numOldLines, numNewLines):
        checkNonNegativeInt(numOldLines)
        checkNonNegativeInt(numNewLines)
        if numOldLines == 0 and numNewLines == 0:
            raise ValueError("An ExpectedUpdate should have old lines or new lines")
        self._numOldLines = numOldLines
        self._numNewLines = numNewLines
    def getNumOldLines(self):
        return self._numOldLines
    def getNumNewLines(self):
        return self._numNewLines

class ActualUpdate:
    def __init__(self, expectedUpdate, firstNewLine):
        self._expectedUpdate = expectedUpdate
        self._firstNewLine = firstNewLine
    def getNumOldLines(self):
        return self._expectedUpdate.getNumOldLines()
    def getNumNewLines(self):
        return self._expectedUpdate.getNumNewLines()

class Window:
    def __init__(self, lines, first, last):
        checkNonEmptyStringList(lines)
        checkNonNegativeInt(first)
        checkNonNegativeInt(last)
        self._lines = lines
        self._first = first
        self._last = last
    def getNumFirst(self):
        return self._first
    def getLines(self):
        return [self._lines[i] for i in range(self._first, self._last + 1)]
    def isWindowContainsFirstLine(self):
        return self._first == 0
    def isWindowContainsLastLine(self):
        return self._last == len(self._lines) - 1
    def widen(self, numContext):
        self.append(numContext)
        return self.prepend(numContext)
    def append(self, numLines):
        self._last = min(self._last + numLines, len(self._lines) - 1)
    def prepend(self, numLines):
        checkNonNegativeInt(numLines)
        newFirst = max(self._first - numLines, 0)
        numPrepended = self._first - newFirst
        self._first = newFirst
        return numPrepended
    def hasOverlap(self, other):
        if not isinstance(other, Window):
            raise TypeError("Should be Window")
        if self._lines != other._lines:
            raise ValueError("Windows should be about the same list of strings")
        return other._first <= self._last + 1
    def join(self, other):
        if not isinstance(other, Window):
            raise TypeError("Should be Window")
        if not self.hasOverlap(other):
            raise ValueError("Should have overlap")
        if not self._first <= other._first:
            raise ValueError("When joining, the first Window comes first")
        numPrepended = other._first - self._first
        return Window(self._lines, self._first, other._last), numPrepended

def actualUpdateToWindow(newLines, actualUpdate):
    checkNonEmptyStringList(newLines)
    if not isinstance(actualUpdate, ActualUpdate):
        raise TypeError("actualUpdate should have type ActualUpdate")
    lines = newLines
    first = actualUpdate._firstNewLine
    last = first + actualUpdate.getNumNewLines() - 1
    return Window(lines, first, last)

class Highlight:
    def __init__(self, relFirst, relLast):
        checkNonNegativeInt(relFirst)
        checkNonNegativeInt(relLast)
        if relFirst > relLast:
            raise ValueError("relFirst should be <= relLast")
        self._relFirst = relFirst
        self._relLast = relLast
    def shift(self, numLines):
        checkNonNegativeInt(numLines)
        self._relFirst += numLines
        self._relLast += numLines
    def getHighlights(self):
        return list(range(self._relFirst, self._relLast + 1))

def copyHighlight(h):
    if not isinstance(h, Highlight):
        raise TypeError("Highlight expected")
    return Highlight(h._relFirst, h._relLast)

def windowToHighlight(w):
    return Highlight(0, w._last - w._first)

class HighlightedWindow:
    def __init__(self, w):
        if not isinstance(w, Window):
            raise TypeError("Should be Window")
        self._window = w
        self._highlights = []
    def getNumFirst(self):
        return self._window.getNumFirst()
    def getLines(self):
        return self._window.getLines()
    def isWindowContainsFirstLine(self):
        return self._window.isWindowContainsFirstLine()
    def isWindowContainsLastLine(self):
        return self._window.isWindowContainsLastLine()
    def getHighlights(self):
        result = []
        for h in self._highlights:
            result.extend(h.getHighlights())
        return result
    def highlightAll(self):
        h = windowToHighlight(self._window)
        self._highlights.append(h)
    def append(self, numLines):
        self._window.append(numLines)
    def prepend(self, numLines):
        numPrepended = self._window.prepend(numLines)
        for h in self._highlights:
            h.shift(numPrepended)
    def hasOverlap(self, other):
        return self._window.hasOverlap(other._window)
    def join(self, other):
        newWindow, numPrepended = self._window.join(other._window)
        result = HighlightedWindow(newWindow)
        for h in self._highlights:
            result._highlights.append(h)
        for h in other._highlights:
            newHighlight = copyHighlight(h)
            newHighlight.shift(numPrepended)
            result._highlights.append(newHighlight)
        return result

def sortedByFirst(windows):
    if not type(windows) is list:
        raise TypeError("List expected, which should have Window instances")
    if not all([isinstance(w, HighlightedWindow) for w in windows]):
        raise TypeError("Not all elements are HighlightedWindow")
    return sorted(windows, key=lambda w: w.getNumFirst())

class Comparison:
    def __init__(self, oldLines, newLines, expectedUpdates, comparator):
        self._oldLines = oldLines
        self._newLines = newLines
        self._expectedUpdates = expectedUpdates
        self._comparator = comparator
        self._actualUpdates = None
        self._comparisonError = None
        self.verify()
    def verify(self):
        checkNonEmptyStringList(self._oldLines)
        checkNonEmptyStringList(self._newLines)
        if not type(self._expectedUpdates) is list:
            raise TypeError("self._expectedUpdates should be a list")
    def compare(self):
        currentOldLine = 0
        currentNewLine = 0
        currentExpectedUpdate = 0
        self._actualUpdates = []
        while currentOldLine < len(self._oldLines) and currentNewLine < len(self._newLines):
            if self._comparator(self._oldLines[currentOldLine], self._newLines[currentNewLine]):
                currentOldLine += 1
                currentNewLine += 1
            else:
                if currentExpectedUpdate >= len(self._expectedUpdates):
                    self._comparisonError = 'Unexpected difference, oldLine = "{0}", newLine = "{1}"'.format(self._oldLines[currentOldLine], self._newLines[currentNewLine])
                    return
                actualUpdate = ActualUpdate(self._expectedUpdates[currentExpectedUpdate], currentNewLine)
                currentOldLine += actualUpdate.getNumOldLines()
                currentNewLine += actualUpdate.getNumNewLines()
                currentExpectedUpdate += 1
                self._actualUpdates.append(actualUpdate)
        while currentExpectedUpdate < len(self._expectedUpdates):
            actualUpdate = ActualUpdate(self._expectedUpdates[currentExpectedUpdate], currentNewLine)
            currentOldLine += actualUpdate.getNumOldLines()
            currentNewLine += actualUpdate.getNumNewLines()
            currentExpectedUpdate += 1
            self._actualUpdates.append(actualUpdate)
        if currentOldLine != len(self._oldLines):
            self._comparisonError = "Not all existing lines have been explained by the expected updates"
            return
        if currentNewLine != len(self._newLines):
            self._comparisonError = "Not all new lines have been explained by the expected updates"
            return
    def hasComparisonError(self):
        return self._comparisonError is not None
    def getComparisonError(self):
        return self._comparisonError
    def getWindows(self):
        return [HighlightedWindow(actualUpdateToWindow(self._newLines, actual)) for actual in self._actualUpdates]

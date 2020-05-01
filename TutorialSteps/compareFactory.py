import yaml

from .treeCompare import Snippet
from .treeCompare import FileAddDifference
from .treeCompare import FileDeleteDifference
from .treeCompare import FileModifyDifference
from .treeCompare import RelPath
from .treeCompare import Change

def createFileDifferences(openedYamlFile):
    try:
        parsedYaml = yaml.safe_load(openedYamlFile)
    except yaml.YAMLError as ex:
        return None, None, "Invalid YAML syntax: " + str(ex)
    if not type(parsedYaml) is list:
        return None, None, "YAML should be a list"
    if not all([type(item) is dict for item in parsedYaml]):
        return None, None, "In YAML, all top-level list items should be a dictionary"
    if not all([len(itemDict) == 1 for itemDict in parsedYaml]):
        return None, None, "In YAML, every top-level line should be like ' - file|snippet:'"
    snippetItems = []
    fileItems = []
    predecessorItems = []
    for itemDict in parsedYaml:
        if "snippet" in itemDict:
            snippetItems.append(itemDict)
        elif "file" in itemDict:
            fileItems.append(itemDict)
        elif "predecessor" in itemDict:
            predecessorItems.append(itemDict)
        else:
            error = "At top level, only '- snippet' or '- file' allowed"
            return
    predecessor, error = _getPredecessor(predecessorItems)
    if error is not None:
        return None, None, error
    snippets, error = _getSnippets(snippetItems)
    if error is not None:
        return None, predecessor, error
    result, error = _getFileComparisons(fileItems, snippets)
    return result, predecessor, error

def _getPredecessor(predecessorItems):
    if len(predecessorItems) >= 2:
        return None, "Duplicate predecessor"
    if len(predecessorItems) == 0:
        return None, None
    predecessor = predecessorItems[0]["predecessor"]
    if not type(predecessor) is str:
        return None, "Predecessor should be a string"
    return predecessor, None

def _getSnippets(origSnippetItems):
    snippetItems = [orig["snippet"] for orig in origSnippetItems]
    if not all(type(item) is dict for item in snippetItems):
        return None, "Within a snippet, only key: value items are allowed"
    allowedKeys = {"name", "markup", "context", "before", "after"}
    snippets = dict()
    for item in snippetItems:
        actualKeys = set(item.keys())
        invalidKeys = actualKeys - allowedKeys
        if len(invalidKeys) >= 1:
            return None, "Within snippet, found invalid keys {0}".format(", ".join(invalidKeys))
        if not "name" in actualKeys:
            return None, "Snippet should have a name"
        if item["name"] in snippets:
            return None, "Dupplicate snippet definition for name {0}".format(item["name"])
        hasContext = "context" in actualKeys
        hasBeforeAndAfter = "before" in actualKeys and "after" in actualKeys
        isBeforeAndAfterOmitted = (not "before" in actualKeys) and (not "after" in actualKeys)
        if not (hasBeforeAndAfter or isBeforeAndAfterOmitted):
            return None, "Either omit 'before' and 'after' or add them both"
        if hasContext and hasBeforeAndAfter:
            return None, "Adding 'context' and 'before' and 'after' is ambiguous"
        if (not hasContext) and (not hasBeforeAndAfter):
            return None, "Add 'context' or 'before' and 'after'"
        newSnippet = Snippet(item["name"])
        if hasContext:
            newSnippet.setNumBefore(item["context"])
            newSnippet.setNumAfter(item["context"])
        else:
            newSnippet.setNumBefore(item["before"])
            newSnippet.setNumAfter(item["after"])
        newSnippet.setMarkupLanguage(item["markup"])
        snippets[item["name"]] = newSnippet
    return snippets, None
def _getFileComparisons(origFileItems, snippets):
    fileItems = [item["file"] for item in origFileItems]
    if not all(type(item) is dict for item in fileItems):
        return None, "After '- file: ', a dictionary must follow"
    minKeySet = {"path", "change"}
    if not all([set(item.keys()) & minKeySet == minKeySet for item in fileItems]):
        return None, "Every '- file' should have 'path:' and 'change:' dictionary keys"
    fileDiffs = []
    error = None
    for item in fileItems:
        path, error = _checkAndGetPath(item["path"])
        if error is not None:
            return None, "Invalid path: " + error
        if item["change"] == "add":
            newFileDiff, error = _getFileDiffAdd(item, path)
        elif item["change"] == "del":
            newFileDiff, error = _getFileDiffDel(item, path)
        elif type(item["change"] is dict):
            newFileDiff, error = _getFileDiffModify(item["change"], path, snippets)
        else:
            error = "Line '- file:' should define add, del or a list of expected modifications"
        if error is not None:
            return None, error
        fileDiffs.append(newFileDiff)
    return fileDiffs, None
def _checkAndGetPath(pathStr):
    if not type(pathStr) is str:
        return None, "Path should be a string"
    if "\\" in pathStr:
        return None, "Path should be unix-style, use / to separate directories"
    if pathStr != pathStr.strip():
        return None, "Did not expect leading or trailing spaces"
    if pathStr[0] == "/":
        return None, "No absolute path allowed, do not start with /"
    result = pathStr.split("/")
    if not type(result) is list:
        raise TypeError("List expected")
    return result, None
def _getFileDiffAdd(item, path):
    return FileAddDifference(RelPath(path)), None
def _getFileDiffDel(item, path):
    return FileDeleteDifference(RelPath(path)), None
def _getFileDiffModify(changes, path, snippets):
    if not type(changes) is list:
        return None, "The changes of a file modifications should form a list"
    if not all([type(item) is dict for item in changes]):
        return None, "Each file change should be a dict"
    result = FileModifyDifference(RelPath(path))
    for change in changes:
        if not "snippet" in change:
            return None, "Change does not have snippet name"
        snippetOfChange = snippets[change["snippet"]]
        doHighlight = "highlight" in change
        numOld, numNew, error = _getLineCountsOfChange(change)
        if error is not None:
            return None, error
        result.addChange(Change(numOld, numNew, doHighlight, snippetOfChange))
    return result, None
def _getLineCountsOfChange(change):
    if "insert" in change:
        if len({"old", "new"} & set(change.keys())) >= 1:
            return None, None, "Change should either have 'insert' or 'old' and 'new', not both"
        return 0, change["insert"], None
    else:
        if not ("old" in change and "new" in change):
            return None, None, "If change is not 'insert', it should both have 'old' and 'new'"
        return change["old"], change["new"], None

from .directoryTree import DirectoryTree
from .compareFactory import createFileDifferences

META_YML = "meta.yml"

class OldAndNew:
    def __init__(self, old, new):
        if not (old is None or isinstance(old, DirectoryTree)):
            raise TypeError("DirectoryTree expected")
        if not isinstance(new, DirectoryTree):
            raise TypeError("DirectoryTree expected")
        self._old = old
        self._new = new
    def getOld(self):
        return self._old
    def getNew(self):
        return self._new

class SortItem:
    def __init__(self, directory, index):
        if not isinstance(directory, DirectoryTree):
            raise TypeError("DirectoryTree expected")
        if not type(index) is int:
            raise TypeError("index should be int")
        self._directory = directory
        self._name = directory.getLastComponent()
        self._index = index
    def getDirectory(self):
        return self._directory
    def getName(self):
        return self._name
    def getIndex(self):
        return self._index

def sortDirectories(directories):
    if not type(directories) is list:
        raise TypeError("List expected, should hold DirectoryTree")
    if not all([isinstance(item, DirectoryTree) for item in directories]):
        raise TypeError("Every list item should be a DirectoryTree")
    sortItems = dict()
    for i in range(0, len(directories)):
        name = directories[i].getLastComponent()
        sortItems[name] = SortItem(directories[i], i)
    result = []
    for i in range(0, len(directories)):
        stepName = directories[i].getLastComponent()
        with directories[i].openFile(META_YML) as f:
            dummy, predecessor, error = createFileDifferences(f)
        if error is not None:
            return None, "Could not parse {0}/{1}: {2}".format(stepName, META_YML, error)
        if i == 0 and predecessor is not None:
            return None, "First directory should not have a predecessor"
        if predecessor is not None and sortItems[predecessor].getIndex() >= i:
            return None, "Predecessors cannot come after the present directory"
        if i == 0:
            old = None
        elif predecessor is not None:
            old = sortItems[predecessor].getDirectory()
        else:
            old = directories[i-1]
        result.append(OldAndNew(old, directories[i]))
    return result, None

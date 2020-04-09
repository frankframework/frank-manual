from .gitDirectoryTree import GitDirectoryTree
from .compareFactory import createFileDifferences

META_YML = "meta.yml"

class OldAndNew:
    def __init__(self, old, new):
        if not (old is None or isinstance(old, GitDirectoryTree)):
            raise TypeError("GitDirectoryTree expected")
        if not isinstance(new, GitDirectoryTree):
            raise TypeError("GitDirectoryTree expected")
        self._old = old
        self._new = new
    def getOld(self):
        return self._old
    def getNew(self):
        return self._new

class SortItem:
    def __init__(self, directory, index):
        if not isinstance(directory, GitDirectoryTree):
            raise TypeError("GitDirectoryTree expected")
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
        raise TypeError("List expected, should hold GitDirectoryTree")
    if not all([isinstance(item, GitDirectoryTree) for item in directories]):
        raise TypeError("Every list item should be a GitDirectoryTree")
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

if __name__ == "__main__":

    import unittest

    class TestSortDirectories(unittest.TestCase):
        def test_happy(self):
            root = GitDirectoryTree("testdataSortDirectories")
            theDirectories = root.getSubdirs()
            result, error = sortDirectories(theDirectories)
            if error is not None:
                print(error)
            self.assertIsNone(error)
            self.assertEqual(len(result), 3)
            resultAsTable = [[item.getOld().getLastComponent() if item.getOld() is not None else "none", item.getNew().getLastComponent()] \
                for item in result]
            self.assertEqual(resultAsTable, [["none", "first"], ["first", "second"], ["first", "third"]])
        def test_when_first_dir_has_predecessor_then_error(self):
            root = GitDirectoryTree("testDataSortDirectoriesFirstHasPredecessor")
            theDirectories = root.getSubdirs()
            result, error = sortDirectories(theDirectories)
            self.assertEqual(error, "First directory should not have a predecessor")
        def test_when_predecessor_references_forward_then_error(self):
            root = GitDirectoryTree("testDataSortDirectoriesForwardPredecessor")
            theDirectories = root.getSubdirs()
            result, error = sortDirectories(theDirectories)
            self.assertEqual(error, "Predecessors cannot come after the present directory")

    unittest.main()

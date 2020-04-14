from .sortDirectories import *

if __name__ == "__main__":

    import unittest

    class TestSortDirectories(unittest.TestCase):
        def test_happy(self):
            root = DirectoryTree("TutorialSteps/testdataSortDirectories")
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
            root = DirectoryTree("TutorialSteps/testDataSortDirectoriesFirstHasPredecessor")
            theDirectories = root.getSubdirs()
            result, error = sortDirectories(theDirectories)
            self.assertEqual(error, "First directory should not have a predecessor")
        def test_when_predecessor_references_forward_then_error(self):
            root = DirectoryTree("TutorialSteps/testDataSortDirectoriesForwardPredecessor")
            theDirectories = root.getSubdirs()
            result, error = sortDirectories(theDirectories)
            self.assertEqual(error, "Predecessors cannot come after the present directory")

    unittest.main()

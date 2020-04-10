from .compareFactory import *

if __name__ == "__main__":
    import unittest

    from io import StringIO

    example = """
- file:
    path: addedFile
    change: add
- file:
    path: deletedFile
    change: del
- predecessor: thePredecessor
- file:
    path: someDir/modifiedFile
    change:
        - insert: 1
          snippet: firstSnippet
        - old: 1
          new: 1
          highlight: True
          snippet: secondSnippet
- snippet:
    name: firstSnippet
    markup: xml
    context: 1
- snippet:
    name: secondSnippet
    markup: none
    before: 2
    after: 3"""

    class TestCreateFileDifferences(unittest.TestCase):
        def test_example(self):
            IO = StringIO(example)
            fileComparisons, predecessor, error = createFileDifferences(IO)
            IO.close()
            self.assertIsNone(error)
            self.assertEqual(predecessor, "thePredecessor")
            self.assertEqual(len(fileComparisons), 3)
            self.assertIs(type(fileComparisons[0]), FileAddDifference)
            self.assertIs(type(fileComparisons[1]), FileDeleteDifference)
            self.assertIs(type(fileComparisons[2]), FileModifyDifference)
            fileAddDiff = fileComparisons[0]
            fileDelDiff = fileComparisons[1]
            fileModDiff = fileComparisons[2]
            self.assertEqual(fileAddDiff.getRelFileName(), "addedFile")
            self.assertEqual(fileDelDiff.getRelFileName(), "deletedFile")
            self.assertEqual(fileModDiff.getRelFileName(), "someDir/modifiedFile")
            changes = fileModDiff._changes
            self.assertEqual(2, len(changes))
            self.assertEqual("firstSnippet", changes[0].getSnippetName())
            self.assertEqual(changes[0]._numOld, 0)
            self.assertEqual(changes[0]._numNew, 1)
            self.assertFalse(changes[0]._doHighlight)
            self.assertEqual(changes[0].getSnippet()._numLinesBefore, 1)
            self.assertEqual(changes[0].getSnippet()._numLinesAfter, 1)
            self.assertEqual(changes[0].getSnippet()._markupLanguage, "xml")
            self.assertEqual(changes[1].getSnippetName(), "secondSnippet")
            self.assertTrue(changes[1]._doHighlight)
            self.assertEqual(changes[1]._numOld, 1)
            self.assertEqual(changes[1]._numNew, 1)
            self.assertEqual(changes[1].getSnippet()._numLinesBefore, 2)
            self.assertEqual(changes[1].getSnippet()._numLinesAfter, 3)
            self.assertEqual(changes[1].getSnippet()._markupLanguage, "none")

    unittest.main()

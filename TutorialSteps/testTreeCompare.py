from .treeCompare import *

if __name__ == "__main__":
    import unittest

    class TestRelPath(unittest.TestCase):
        def test_it(self):
            r = RelPath(["parent", "child"])
            self.assertEqual("parent/child", str(r))

    base = """line 1""".replace("\r\n", "\n").split("\n")

    extraLine = """line 1
line 2""".replace("\r\n", "\n").split("\n")

    snippetBase2ExtraLine = """.. code-block:: none

   ...
   line 2""".replace("\r\n", "\n").split("\n")

    snippetBase2ExtraLineHighlightContextXml = """.. code-block:: xml
   :emphasize-lines: 2

   line 1
   line 2""".replace("\r\n", "\n").split("\n")

    different = """other line 1
other line 2
other line 3""".replace("\r\n", "\n").split("\n")

    oldTwoWindows = """line 1
line 2
line 3""".replace("\r\n", "\n").split("\n")

    newTwoWindows = """line 1
inserted
line 2
replaced""".replace("\r\n", "\n").split("\n")

    twoWindowsCombinedRst = """.. code-block:: none

   line 1
   inserted
   line 2
   replaced""".replace("\r\n", "\n").split("\n")

    twoWindowsFirstRst = """.. code-block:: none

   ...
   inserted
   ...""".replace("\r\n", "\n").split("\n")

    twoWindowsSecondRst = """.. code-block:: none

   ...
   replaced""".replace("\r\n", "\n").split("\n")

    class TestTreeComparison(unittest.TestCase):
        def test_when_no_expectations_and_equal_file_then_no_errors(self):
            comparison = TreeComparison([])
            comparison.addOld(RelPath(["fileName"]), base)
            comparison.addNew(RelPath(["fileName"]), base)
            snippets, errors = comparison.run()
            self.assertIsNotNone(snippets)
            self.assertEqual([], snippets)
            self.assertIsNone(errors)
        def test_when_no_expectations_and_modified_file_then_errors(self):
            comparison = TreeComparison([])
            comparison.addOld(RelPath(["fileName"]), base)
            comparison.addNew(RelPath(["fileName"]), different)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def test_when_file_modify_expected_and_satisfied_then_snippet(self):
            mySnippet = Snippet("mySnippet")
            change = Change(0, 1, False, mySnippet)
            fileDiff = FileModifyDifference(RelPath(["fileName"]))
            fileDiff.addChange(change)
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), base)
            comparison.addNew(RelPath(["fileName"]), extraLine)
            snippets, errors = comparison.run()
            self.assertIsNone(errors)
            self.assertEqual(len(snippets), 1)
            self.assertEqual(snippets[0].getName(), "mySnippet")
            self.assertEqual(snippets[0].getLines(), snippetBase2ExtraLine)
        def test_when_file_modify_expected_and_satisfied_then_snippet_with_context_highlight_language(self):
            mySnippet = Snippet("mySnippet")
            mySnippet.setMarkupLanguage("xml")
            mySnippet.setNumBefore(1)
            mySnippet.setNumAfter(1)
            change = Change(0, 1, True, mySnippet)
            fileDiff = FileModifyDifference(RelPath(["fileName"]))
            fileDiff.addChange(change)
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), base)
            comparison.addNew(RelPath(["fileName"]), extraLine)
            snippets, errors = comparison.run()
            self.assertIsNone(errors)
            self.assertEqual(len(snippets), 1)
            self.assertEqual(snippets[0].getName(), "mySnippet")
            self.assertEqual(snippets[0].getLines(), snippetBase2ExtraLineHighlightContextXml)
        def test_when_file_modify_expected_but_delete_found_then_error(self):
            mySnippet = Snippet("mySnippet")
            change = Change(0, 1, False, mySnippet)
            fileDiff = FileModifyDifference(RelPath(["fileName"]))
            fileDiff.addChange(change)
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), base)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def test_when_file_modify_expected_but_add_found_then_error(self):
            mySnippet = Snippet("mySnippet")
            change = Change(0, 1, False, mySnippet)
            fileDiff = FileModifyDifference(RelPath(["fileName"]))
            fileDiff.addChange(change)
            comparison = TreeComparison([fileDiff])
            comparison.addNew(RelPath(["fileName"]), base)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def test_when_file_add_expected_and_satisfied_then_no_error(self):
            fileDiff = FileAddDifference(RelPath(["fileName"]))
            comparison = TreeComparison([fileDiff])
            comparison.addNew(RelPath(["fileName"]), base)
            snippets, errors = comparison.run()
            self.assertIsNotNone(snippets)
            self.assertEqual([], snippets)
            self.assertIsNone(errors)
        def test_when_file_add_expected_but_file_deleted_then_error(self):
            fileDiff = FileAddDifference(RelPath(["fileName"]))
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), base)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def test_when_file_delete_expected_and_satisfied_then_no_error(self):
            fileDiff = FileDeleteDifference(RelPath(["fileName"]))
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), base)
            snippets, errors = comparison.run()
            self.assertIsNotNone(snippets)
            self.assertEqual([], snippets)
            self.assertIsNone(errors)
        def test_when_file_delete_expected_but_file_added_then_error(self):
            fileDiff = FileDeleteDifference(RelPath(["fileName"]))
            comparison = TreeComparison([fileDiff])
            comparison.addNew(RelPath(["fileName"]), base)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def test_when_expectation_about_unknown_file_then_error(self):
            fileDiff = FileDeleteDifference(RelPath(["fileName"]))
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["otherFileName"]), base)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def test_two_windows_when_one_rst_requested_and_overlap_then_rst_from_join(self):
            mySnippet = Snippet("mySnippet")
            mySnippet.setNumBefore(2)
            mySnippet.setNumAfter(2)
            firstChange = Change(0, 1, False, mySnippet)
            secondChange = Change(1, 1, False, mySnippet)
            fileDiff = FileModifyDifference(RelPath(["fileName"]))
            fileDiff.addChange(firstChange)
            fileDiff.addChange(secondChange)
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), oldTwoWindows)
            comparison.addNew(RelPath(["fileName"]), newTwoWindows)
            snippets, errors = comparison.run()
            self.assertIsNone(errors)
            self.assertEqual(len(snippets), 1)
            self.assertEqual(snippets[0].getName(), "mySnippet")
            self.assertEqual(snippets[0].getLines(), twoWindowsCombinedRst)
        def test_two_windows_when_one_rst_requested_and_no_overlap_then_error(self):
            mySnippet = Snippet("mySnippet")
            mySnippet.setNumBefore(0)
            mySnippet.setNumAfter(0)
            firstChange = Change(0, 1, False, mySnippet)
            secondChange = Change(1, 1, False, mySnippet)
            fileDiff = FileModifyDifference(RelPath(["fileName"]))
            fileDiff.addChange(firstChange)
            fileDiff.addChange(secondChange)
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), oldTwoWindows)
            comparison.addNew(RelPath(["fileName"]), newTwoWindows)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def test_two_windows_when_two_rst_requested_and_no_overlap_then_two_rst(self):
            myFirstSnippet = Snippet("myFirstSnippet")
            mySecondSnippet = Snippet("mySecondSnippet")
            myFirstSnippet.setNumBefore(0)
            myFirstSnippet.setNumAfter(0)
            mySecondSnippet.setNumBefore(0)
            mySecondSnippet.setNumAfter(0)
            firstChange = Change(0, 1, False, myFirstSnippet)
            secondChange = Change(1, 1, False, mySecondSnippet)
            fileDiff = FileModifyDifference(RelPath(["fileName"]))
            fileDiff.addChange(firstChange)
            fileDiff.addChange(secondChange)
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), oldTwoWindows)
            comparison.addNew(RelPath(["fileName"]), newTwoWindows)
            snippets, errors = comparison.run()
            self.assertIsNone(errors)
            self.assertEqual(len(snippets), 2)
            sortedSnippets = sorted(snippets, key=lambda s: s.getName())
            self.assertEqual(sortedSnippets[0].getName(), "myFirstSnippet")
            self.assertEqual(sortedSnippets[0].getLines(), twoWindowsFirstRst)
            self.assertEqual(sortedSnippets[1].getName(), "mySecondSnippet")
            self.assertEqual(sortedSnippets[1].getLines(), twoWindowsSecondRst)
        def test_two_windows_when_two_rst_requested_but_overlap_then_error(self):
            myFirstSnippet = Snippet("myFirstSnippet")
            mySecondSnippet = Snippet("mySecondSnippet")
            myFirstSnippet.setNumBefore(2)
            myFirstSnippet.setNumAfter(2)
            mySecondSnippet.setNumBefore(2)
            mySecondSnippet.setNumAfter(2)
            firstChange = Change(0, 1, False, myFirstSnippet)
            secondChange = Change(1, 1, False, mySecondSnippet)
            fileDiff = FileModifyDifference(RelPath(["fileName"]))
            fileDiff.addChange(firstChange)
            fileDiff.addChange(secondChange)
            comparison = TreeComparison([fileDiff])
            comparison.addOld(RelPath(["fileName"]), oldTwoWindows)
            comparison.addNew(RelPath(["fileName"]), newTwoWindows)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def test_when_same_snippet_used_for_multiple_files_then_error(self):
            mySnippet = Snippet("mySnippet")
            firstChange = Change(0, 1, False, mySnippet)
            firstFileDiff = FileModifyDifference(RelPath(["fileName"]))
            firstFileDiff.addChange(firstChange)
            secondChange = Change(0, 1, False, mySnippet)
            secondFileDiff = FileModifyDifference(RelPath(["otherFileName"]))
            secondFileDiff.addChange(secondChange)
            comparison = TreeComparison([firstFileDiff, secondFileDiff])
            comparison.addOld(RelPath(["fileName"]), base)
            comparison.addNew(RelPath(["fileName"]), extraLine)
            comparison.addOld(RelPath(["otherFileName"]), base)
            comparison.addNew(RelPath(["otherFileName"]), extraLine)
            snippets, errors = comparison.run()
            self.assertNonEmptyStringList(errors)
        def assertNonEmptyStringList(self, sl):
            self.assertIs(type(sl), list)
            self.assertTrue(len(sl) >= 1)
            for item in sl:
                self.assertIs(type(item), str)
            
    unittest.main()

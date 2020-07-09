from .stringListCompare import *

if __name__ == "__main__":

    import unittest

    class TestGetIndentAndCheck(unittest.TestCase):
        def test_if_properly_indented_then_get_indent(self):
            indent, err = getIndentAndCheck("   text")
            self.assertTrue(err is None)
            self.assertEqual(3, indent)
            indent, err = getIndentAndCheck("text")
            self.assertTrue(err is None)
            self.assertEqual(0, indent)
        def test_if_has_tab_then_error(self):
            indent, err = getIndentAndCheck(" \t text")
            self.assertTrue(type(err) is str)
        def test_if_empty_line_then_indent_none(self):
            indent, err = getIndentAndCheck("")
            self.assertIsNone(err)
            self.assertIsNone(indent)

    class TestComparators(unittest.TestCase):
        def test_comparatorIndentInsensitive(self):
            self.assertTrue(comparatorIndentInsensitive("  monkey  ", " monkey   "))
            self.assertFalse(comparatorIndentInsensitive("donkey", "kong"))
        def test_comparatorIndentSensitive(self):
            self.assertTrue(comparatorIndentSensitive("monkey", "monkey"))
            self.assertFalse(comparatorIndentSensitive("  monkey  ", " monkey   "))
            self.assertFalse(comparatorIndentSensitive("donkey", "Kont"))

    class TestComparison(unittest.TestCase):
        def test_if_old_and_new_equal_and_no_expected_updates_then_ok_one_line(self):
            comparison = Comparison(["monkey"], ["monkey"], [], comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
        def test_if_old_and_new_equal_and_no_expected_updates_then_ok_two_line(self):
            comparison = Comparison(["monkey", "tail"], ["monkey", "tail"], [], comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
        def test_if_old_and_new_equal_and_expected_update_then_nok(self):
            comparison = Comparison(["monkey"], ["monkey"], [ExpectedUpdate(0, 1)], comparatorIndentSensitive)
            comparison.compare()
            self.assertTrue(comparison.hasComparisonError())
        def test_if_extra_old_line_then_nok(self):
            comparison = Comparison(["monkey", "tail"], ["monkey"], [], comparatorIndentSensitive)
            comparison.compare()
            self.assertTrue(comparison.hasComparisonError())
        def test_if_extra_new_line_then_nok(self):
            comparison = Comparison(["monkey"], ["monkey", "tail"], [], comparatorIndentSensitive)
            comparison.compare()
            self.assertTrue(comparison.hasComparisonError())
        def test_if_expected_insert_satisfied_then_ok(self):
            comparison = Comparison(["monkey", "tail"], ["monkey", "gets", "tail"], [ExpectedUpdate(0, 1)], comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
        def test_if_expected_replace_satisfied_then_ok(self):
            comparison = Comparison(["monkey", "has", "tail"], ["monkey", "gets", "tail"], [ExpectedUpdate(1, 1)], comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
        def test_if_expected_update_count_shortage_then_nok(self):
            comparison = Comparison(["monkey", "tail"], ["monkey", "has", "tail"], [ExpectedUpdate(0, 2)], comparatorIndentSensitive)
            comparison.compare()
            self.assertTrue(comparison.hasComparisonError())
        def test_if_expected_update_count_exceeded_then_nok(self):
            comparison = Comparison(["monkey", "tail"], ["monkey", "has", "a", "tail"], [ExpectedUpdate(0, 1)], comparatorIndentSensitive)
            comparison.compare()
            self.assertTrue(comparison.hasComparisonError())
        def test_if_comparator_indent_insensitive_and_only_indent_diff_then_ok(self):
            comparison = Comparison(["monkey"], ["  monkey  "], [], comparatorIndentInsensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
        def test_if_comparator_indent_sensitive_and_only_indent_diff_then_nok(self):
            comparison = Comparison(["monkey"], ["  monkey  "], [], comparatorIndentSensitive)
            comparison.compare()
            self.assertTrue(comparison.hasComparisonError())
        def test_if_expected_insert_satisfied_at_end_then_ok(self):
            comparison = Comparison(["monkey"], ["monkey", "added"], [ExpectedUpdate(0, 1)], comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
        def test_if_delete_satisfied_at_end_then_ok(self):
            comparison = Comparison(["monkey", "removed"], ["monkey"], [ExpectedUpdate(1, 0)], comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())

    class TestWindow(unittest.TestCase):
        def test_winden_window_can_take_one_line(self):
            w = Window(["zero", "one", "two", "three", "four"], 2, 3)
            w.widen(1)
            self.assertEqual(w.getLines(), ["one", "two", "three", "four"])
        def test_window_widen_respects_end_of_file(self):
            w = Window(["zero", "one", "two", "three", "four"], 2, 3)
            w.widen(2)
            self.assertEqual(w.getLines(), ["zero", "one", "two", "three", "four"])
        def test_window_widen_respects_start_of_file(self):
            w = Window(["zero", "one", "two", "three", "four"], 1, 2)
            w.widen(2)
            self.assertEqual(w.getLines(), ["zero", "one", "two", "three", "four"])
        def test_if_windows_dont_touch_then_no_overlap(self):
            lines = ["zero", "one", "two", "three", "four"]
            firstWindow = Window(lines, 0, 1)
            secondWindow = Window(lines, 3, 4)
            self.assertFalse(firstWindow.hasOverlap(secondWindow))
        def test_if_windows_touch_then_overlap_and_can_join(self):
            lines = ["zero", "one", "two", "three", "four", "five"]
            firstWindow = Window(lines, 1, 2)
            secondWindow = Window(lines, 3, 4)
            self.assertTrue(firstWindow.hasOverlap(secondWindow))
            joinResult, numPrepended = firstWindow.join(secondWindow)
            self.assertEqual(["one", "two", "three", "four"], joinResult.getLines())
            self.assertEqual(2, numPrepended)
        def test_if_windows_overlap_then_overlap_and_can_join(self):
            lines = ["zero", "one", "two", "three", "four", "five"]
            firstWindow = Window(lines, 1, 2)
            secondWindow = Window(lines, 2, 4)
            self.assertTrue(firstWindow.hasOverlap(secondWindow))
            joinResult, numPrepended = firstWindow.join(secondWindow)
            self.assertEqual(["one", "two", "three", "four"], joinResult.getLines())
            self.assertEqual(1, numPrepended)

    class TestHighlight(unittest.TestCase):
        def test_it(self):
            h = Highlight(3, 5)
            self.assertEqual([3, 4, 5], h.getHighlights())
            h.shift(3)
            self.assertEqual([6, 7, 8], h.getHighlights())

    class TestHighlightedWindow(unittest.TestCase):
        def test_when_prepended_then_highlights_shifted(self):
            comparison = Comparison( \
                ["one",                 "four"], \
                ["one", "two", "three", "four"], \
                [ExpectedUpdate(0, 2)], \
                comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
            windows = comparison.getWindows()
            self.assertEqual(len(windows), 1)
            windows[0].highlightAll()
            self.assertEqual(windows[0].getNumFirst(), 1)
            self.assertEqual(len(windows[0].getLines()), 2)
            highlights = windows[0]._highlights
            self.assertEqual(len(highlights), 1)
            self.assertEqual(highlights[0]._relFirst, 0)
            self.assertEqual(highlights[0]._relLast, 1)
            windows[0].prepend(1)
            self.assertEqual(windows[0].getNumFirst(), 0)
            self.assertEqual(len(windows[0].getLines()), 3)
            highlights = windows[0]._highlights
            self.assertEqual(len(highlights), 1)
            self.assertEqual(highlights[0]._relFirst, 1)
            self.assertEqual(highlights[0]._relLast, 2)
        def test_when_two_windows_touch_then_joined_correctly_first_highlight(self):
            comparison = Comparison( \
                ["one",                 "four", "five",        "seven"], \
                ["one", "two", "three", "four", "five", "six", "seven"], \
                [ExpectedUpdate(0, 2), ExpectedUpdate(0, 1)], \
                comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
            windows = comparison.getWindows()
            self.assertEqual(len(windows), 2)
            windows[0].highlightAll()
            windows[0].prepend(1)
            windows[0].append(1)
            windows[1].prepend(1)
            windows[1].append(1)
            self.assertTrue(windows[0].hasOverlap(windows[1]))
            joinWindow = windows[0].join(windows[1])
            self.assertEqual(joinWindow.getLines(), ["one", "two", "three", "four", "five", "six", "seven"])
            self.assertEqual([n+1 for n in joinWindow.getHighlights()], [2, 3])
        def test_when_two_windows_touch_then_joined_correctly_second_highlight(self):
            comparison = Comparison( \
                ["one",        "three", "four",                "seven"], \
                ["one", "two", "three", "four", "five", "six", "seven"], \
                [ExpectedUpdate(0, 1), ExpectedUpdate(0, 2)], \
                comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
            windows = comparison.getWindows()
            windows[1].highlightAll()
            windows[0].prepend(1)
            windows[0].append(1)
            windows[1].prepend(1)
            windows[1].append(1)
            self.assertTrue(windows[0].hasOverlap(windows[1]))
            joinWindow = windows[0].join(windows[1])
            self.assertEqual(joinWindow.getLines(), ["one", "two", "three", "four", "five", "six", "seven"])
            self.assertEqual([n+1 for n in joinWindow.getHighlights()], [5, 6])
        def test_when_two_windows_dont_touch_then_not_joinable(self):
            comparison = Comparison( \
                ["one",        "three", "four", "five",        "seven"], \
                ["one", "two", "three", "four", "five", "six", "seven"], \
                [ExpectedUpdate(0, 1), ExpectedUpdate(0, 1)], \
                comparatorIndentSensitive)
            comparison.compare()
            self.assertFalse(comparison.hasComparisonError())
            windows = comparison.getWindows()
            windows[0].prepend(1)
            windows[0].append(1)
            windows[1].prepend(1)
            windows[1].append(1)
            self.assertFalse(windows[0].hasOverlap(windows[1]))
        def test_sort(self):
            lines = ["aap", "noot", "mies"]
            w1 = HighlightedWindow(Window(lines, 1, 1))
            w2 = HighlightedWindow(Window(lines, 2, 2))
            self.assertEqual(sortedByFirst([w2, w1]), [w1, w2])
            self.assertEqual(sortedByFirst([w1, w2]), [w1, w2])
    unittest.main()
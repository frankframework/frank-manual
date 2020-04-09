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
                    self._comparisonError = "Unexpected difference, oldLine = {0}, newLine = {1}".format(currentOldLine, currentNewLine)
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
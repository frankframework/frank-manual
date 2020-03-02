comparatorIndentInsensitive = lambda first, second: first.strip() == second.strip()
comparatorIndentSensitive = lambda first, second: first == second

class ExpectedUpdate:
    def __init__(self, numOldLines, numNewLines):
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
        if not type(self._oldLines) is list:
            raise TypeError("self._oldLines is not a list")
        if not type(self._newLines) is list:
            raise TypeError("self._newLines is not a list")
        if not all([type(line) is str for line in self._oldLines]):
            raise TypeError("self._oldLines should be a list of strings")
        if not all([type(line) is str for line in self._newLines]):
            raise TypeError("self._newLines should be a list of string")
        if len(self._oldLines) == 0:
            raise ValueError("self._oldLines should not be empty")
        if len(self._newLines) == 0:
            raise ValueError("self._newLines should not be empty")
        if not type(self._expectedUpdates) is list:
            raise TypeError("self._expectedUpdates should be a list, but is of type")
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
        if currentExpectedUpdate != len(self._expectedUpdates):
            self._comparisonError = "Expected {0} updates, but less updates found".format(len(self._expectedUpdates))
            return
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

if __name__ == "__main__":

    import unittest

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

    unittest.main()
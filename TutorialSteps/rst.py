from stringListCompare import HighlightedWindow
from stringListCompare import Window
from stringListCompare import Highlight
from stringListCompare import unindentAndCheck
from stringListCompare import copyHighlight

def makeRst(w, markupLanguage):
    if not isinstance(w, HighlightedWindow):
        raise TypeError("w should be HighlightedWindow")
    if not type(markupLanguage) is str:
        raise TypeError("markupLanguage should be a string")
    unindentedLines, err = unindentAndCheck(w.getLines())
    highlights = w.getHighlights()
    if err is not None:
        return None, err
    body = ["   " + line for line in unindentedLines]
    header = ".. code-block:: " + markupLanguage
    optionalStartEllipsis = []
    if not w.isWindowContainsFirstLine():
        optionalStartEllipsis = ["   ..."]
        highlights = [n+1 for n in highlights]
    optionalEndEllipsis = []
    if not w.isWindowContainsLastLine():
        optionalEndEllipsis = ["   ..."]
    emphasizeNums = [n+1 for n in highlights]
    optionalEmphasize = []
    if len(emphasizeNums) >= 1:
        optionalEmphasize = ["   :emphasize-lines: " + ", ".join([str(n) for n in emphasizeNums])]
    return [header] + optionalEmphasize + [""] + optionalStartEllipsis + body + optionalEndEllipsis, None

if __name__ == "__main__":
    import unittest

    class TestMakeRst(unittest.TestCase):
        def testNoHighlightAllEllipsis(self):
            lines = ["zero", "  one", "    two", "  three", "four"]
            base = Window(lines, 1, 3)
            w = HighlightedWindow(base)
            expectedResult = [ \
                ".. code-block:: none", \
                "", \
                "   ...", \
                "   one", \
                "     two", \
                "   three", \
                "   ..."]
            actualResult, err = makeRst(w, "none")
            self.assertTrue(err is None)
            self.assertEqual(actualResult, expectedResult)
        def testNoHighlightNoEllipsis(self):
            lines = ["zero"]
            base = Window(lines, 0, 0)
            w = HighlightedWindow(base)
            expectedResult = [ \
                ".. code-block:: none", \
                "", \
                "   zero"]
            actualResult, err = makeRst(w, "none")
            self.assertTrue(err is None)
            self.assertEqual(actualResult, expectedResult)
        def testHighlightAndAllEllipsis(self):
            lines = ["zero", "one", "two", "three"]
            base = Window(lines, 1, 2)
            w = HighlightedWindow(base)
            w.highlightAll()
            expectedResult = [ \
                ".. code-block:: none", \
                "   :emphasize-lines: 2, 3", \
                "", \
                "   ...", \
                "   one", \
                "   two", \
                "   ..."]
            actualResult, err = makeRst(w, "none")
            self.assertTrue(err is None)
            self.assertEqual(actualResult, expectedResult)
        def testHighlightNoEllipsis(self):
            lines = ["zero"]
            base = Window(lines, 0, 0)
            w = HighlightedWindow(base)
            w.highlightAll()
            expectedResult = [ \
                ".. code-block:: none", \
                "   :emphasize-lines: 1", \
                "", \
                "   zero"]
            actualResult, err = makeRst(w, "none")
            self.assertTrue(err is None)
            self.assertEqual(actualResult, expectedResult)
            
    unittest.main()
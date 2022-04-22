from .rst import *

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
        def testTabIndentsAreReplacedBySpaces(self):
            lines = ["zero", "\tone", "\t\ttwo", "\tthree", "four"]
            base = Window(lines, 1, 3)
            w = HighlightedWindow(base)
            expectedResult = [ \
                ".. code-block:: none", \
                "", \
                "   ...", \
                "   one", \
                "       two", \
                "   three", \
                "   ..."]
            actualResult, err = makeRst(w, "none")
            self.assertTrue(err is None)
            self.assertEqual(actualResult, expectedResult)

        def testUntab(self):
            self.assertEqual(unTab(""), "")
            self.assertEqual(unTab(" "), " ")
            self.assertEqual(unTab("\t"), "    ")
            self.assertEqual(unTab("\taap"), "    aap")
            self.assertEqual(unTab(" \taap"), "     aap")

    unittest.main()

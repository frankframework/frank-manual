from .stringListCompare import HighlightedWindow
from .stringListCompare import Window
from .stringListCompare import Highlight
from .stringListCompare import unindentAndCheck
from .stringListCompare import copyHighlight

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

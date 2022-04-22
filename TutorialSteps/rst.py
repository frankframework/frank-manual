from .stringListCompare import HighlightedWindow
from .stringListCompare import Window
from .stringListCompare import Highlight
from .stringListCompare import unindentAndCheck
from .stringListCompare import copyHighlight

import re

def makeRst(w, markupLanguage):
    if not isinstance(w, HighlightedWindow):
        raise TypeError("w should be HighlightedWindow")
    if not type(markupLanguage) is str:
        raise TypeError("markupLanguage should be a string")
    unindentedLines, err = unindentAndCheck([unTab(l) for l in w.getLines()])
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

def unTab(line):
    if(len(line) == 0):
        return line
    indexFirstNonSpaceMatch = re.match(r'[^ \t\r\n]', line)
    if indexFirstNonSpaceMatch is None:
        return _untabSpaces(line)
    else:
        indexFirstNonSpace = indexFirstNonSpaceMatch.start()
        startOfLine = line[0:indexFirstNonSpace]
        endOfLine = line[indexFirstNonSpace:]
        return _untabSpaces(startOfLine) + endOfLine

def _untabSpaces(spaces):
    result = ""
    for c in spaces:
        if c == '\t':
            result += "    "
        else:
            result += c
    return result

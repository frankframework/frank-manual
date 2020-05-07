import os
import sys
import subprocess
from zipfile import ZipFile
from fileUtils import makeDirectoryIfNotPresent

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

def walkLines(fname, handler):
    with open(fname, "r") as f:
        for cnt, line in enumerate(f):
            handler(line)

def walkFilesInDirectory(theDirectory, handlerFile):
    for dirname, _, filenames in os.walk(theDirectory):
        for filename in filenames:
            handlerFile(dirname, filename)
    
class ZipWriter:
    def __init__(self, base, zipObj, baseDirInZip):
        self._base = base
        self._zipObj = zipObj
        self._baseDirInZip = baseDirInZip

    def writeFile(self, folderName, fname, toOmit):
        print("INFO: writeFile folderName {0} fname {1}".format(folderName, fname))
        if fname in toOmit:
            print("INFO: Omit from zip: folderName {0} fname {1}".format(folderName, fname))
            return
        original = os.path.join(folderName, fname)
        target = self._getTarget(folderName, fname)
        with open(original, 'rb') as fileToInclude:
            content = fileToInclude.read()
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
        self._zipObj.writestr(target, content)

    def _getTarget(self, folderName, item):
        subDirInZip = os.path.relpath(folderName, self._base)
        if subDirInZip == "." :
            target = item
        else :
            target = os.path.join(subDirInZip, item)
        if self._baseDirInZip is not None:
            target = os.path.join(self._baseDirInZip, target)
        print("INFO: target {0}".format(target))
        return target

def createDownloadZip(target, sourceDir, baseDirInZip, toOmit, onError):
    target = os.path.normpath(target)
    sourceDir = os.path.normpath(sourceDir)
    if not os.path.exists(sourceDir):
        print("ERROR: directory does not exist: {0}".format(sourceDir))
        onError()
        return
    if not os.path.isdir(sourceDir):
        print("ERROR: not a directory: {0}".format(sourceDir))
        onError()
        return
    if not os.listdir(sourceDir):
        print("ERROR: empty directory {0}".format(sourceDir))
        onError()
        return
    if target[-4:] != ".zip":
        print("ERROR: not a .zip file: {0}".format(target))
        onError()
        return
    if baseDirInZip is not None:
        if "\\" in baseDirInZip:
            print("ERROR: Found windows path separator in baseDirInZip, no path separators allowed: " + baseDirInZip)
            onError()
            return
        if "/" in baseDirInZip:
            print("ERROR: Found Linux path separator in baseDirInZip, no path separators allowed: " + baseDirInZip)
            onError()
            return
        print("INFO: Creating downloadable file {0} from directory {1}, base dir in zip {2}".format(target, sourceDir, baseDirInZip))
    else:
        print("INFO: Creating downloadable file {0} from directory {1}, without base dir in zip".format(target, sourceDir))
    with ZipFile(target, "w") as z:
        zipWriter = ZipWriter(sourceDir, z, baseDirInZip)
        walkFilesInDirectory(sourceDir, \
            lambda folderName, fname: zipWriter.writeFile(folderName, fname, toOmit))

def makeTargetSubdir(targetFileName, targetDir):
    if not type(targetFileName) is str:
        raise TypeError("String expected")
    if targetFileName == "":
        raise ValueError("Path should not be empty")
    if "\\" in targetFileName:
        raise ValueError("Path is not Linux-style")
    if targetFileName != targetFileName.strip():
        raise ValueError("Path is not stripped")
    if targetFileName[0] == "/":
        raise ValueError("Path is not relative")
    components = targetFileName.split("/")
    if len(components) <= 1:
        return
    subdirComponents = components[0:-1]
    if any(["." in c for c in subdirComponents]):
        raise ValueError("Paths with . or .. not supported")

    makeDirectoryIfNotPresent("/".join(subdirComponents), targetDir)

def createDownloadZipFromLine(line, targetDir, toOmit, onError):
    fields = line.split()
    source = fields[0]
    if len(fields) >= 2 :
        targetFileName = fields[1] + ".zip"
        makeTargetSubdir(targetFileName, targetDir)
        target = os.path.join(targetDir, targetFileName)
    else :
        targetFileName = os.path.basename(source) + ".zip"
        makeTargetSubdir(targetFileName, targetDir)
        target = os.path.join(targetDir, targetFileName)
    baseDirInZip = None
    if len(fields) == 3:
        baseDirInZip = fields[2]
    createDownloadZip(target, source, baseDirInZip, toOmit, onError)

def handleLine(line, targetDir, toOmit, onError):
    line = line.strip()
    if len(line) == 0:
        return
    if line[0] == "#":
        return
    createDownloadZipFromLine(line, targetDir, toOmit, onError)

def createAllDownloadZips(descriptorFile, targetDir, toOmit):
    """
Produce download zips for the Frank!Manual.

    Parameters:
        descriptorFile: Path to configuration file that specifies which
            input directories to zip and which output files to produce.
            See comments in the provided descriptorFile for details on the
            syntax and semantics.
        targetDir: Directory in which download zips are stored.
        toOmit (set): Files to ignore when producing download zips.
            These should be simple filenames without a path. When
            an input file within this set is encountered, it is not
            added to the corresponding zip file.

    This function also replaces Windows line endings by Linux line endings. This way,
    Windows and Linux users will produce download files in which the text files
    have the same line endings.
    """
    makeDirectoryIfNotPresent(targetDir)
    # Workaround because Python 2.7 does not have the nonlocal keyword.
    # In Python 3, we could just have a boolean. Now we use Python 3,
    # so the code can be simplified when time permits.
    dictionaryContainingHasErrors = {"hasErrors": False}
    def onError():
        dictionaryContainingHasErrors["hasErrors"] = True
    walkLines(descriptorFile, lambda line: handleLine(line, targetDir, toOmit, onError))
    if dictionaryContainingHasErrors["hasErrors"]:
        print("*** There were errors creating the download zips!")
    return dictionaryContainingHasErrors["hasErrors"]


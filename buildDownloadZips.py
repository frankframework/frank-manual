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

def walkTrackedFilesInDirectory(theDirectory, handlerFile):
    cmd = "git ls-files {0}".format(theDirectory)
    trackedFiles = subprocess.check_output(cmd, shell=True).splitlines()
    for relPath in trackedFiles:
        folderName, fname = os.path.split(relPath)
        handlerFile(folderName, fname)

class ZipWriter:
    def __init__(self, base, zipObj):
        self._base = base
        self._zipObj = zipObj

    def writeFile(self, folderName, fname, toOmit):
        print "INFO: writeFile folderName {0} fname {1}".format(folderName, fname)
        if fname in toOmit:
            print "INFO: Omit from zip: folderName {0} fname {1}".format(folderName, fname)
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
        print "INFO: target {0}".format(target)
        return target

def createDownloadZip(target, sourceDir, toOmit):
    target = os.path.normpath(target)
    sourceDir = os.path.normpath(sourceDir)
    if not os.path.exists(sourceDir):
        print "ERROR: directory does not exist: {0}".format(sourceDir)
        return
    if not os.path.isdir(sourceDir):
        print "ERROR: not a directory: {0}".format(sourceDir)
        return
    if not os.listdir(sourceDir):
        print "ERROR: empty directory {0}".format(sourceDir)
        return
    if target[-4:] != ".zip":
        print "ERROR: not a .zip file: {0}".format(target)
        return
    print "INFO: Creating downloadable file {0} from directory {1}".format(target, sourceDir)
    with ZipFile(target, "w") as z:
        zipWriter = ZipWriter(sourceDir, z)
        walkTrackedFilesInDirectory(sourceDir, \
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

def createDownloadZipFromLine(line, targetDir, toOmit):
    fields = line.split()
    source = fields[0]
    if len(fields) == 1 :
        targetFileName = os.path.basename(source) + ".zip"
        makeTargetSubdir(targetFileName, targetDir)
        target = os.path.join(targetDir, targetFileName)
    else :
        targetFileName = fields[1] + ".zip"
        makeTargetSubdir(targetFileName, targetDir)
        target = os.path.join(targetDir, targetFileName)
    createDownloadZip(target, source, toOmit)

def handleLine(line, targetDir, toOmit):
    line = line.strip()
    if len(line) == 0:
        return
    if line[0] == "#":
        return
    createDownloadZipFromLine(line, targetDir, toOmit)

def createAllDownloadZips(descriptorFile, targetDir, toOmit):
    makeDirectoryIfNotPresent(targetDir)
    walkLines(descriptorFile, lambda line: handleLine(line, targetDir, toOmit))

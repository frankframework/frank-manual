#!/usr/bin/python

# This script is needed to build the manual for the Frank!framework.
# Within the manual code we want download links to Frank code that
# complements the explanations in the text. This script produces
# these zip files from the subdirectories of the src directory.
#
# This script reads a file "buildDownloadZips.txt". This
# file lists all subdirectories of ibis4manual that need
# to be zipped. These zips appear in directory
# "docs/source/downloads".

import os
import sys
from zipfile import ZipFile

targetDir = os.path.normpath("docs/source/downloads")
downloadsDescriptor = "buildDownloadZips.txt"

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

def walkLines(fname, handler):
    with open(fname, "r") as f:
        for cnt, line in enumerate(f):
            handler(line)

def walkDirectory(theDirectory, handlerFolder, handlerFile):
    for folderName, subFolders, fileNames in os.walk(theDirectory):
        for subFolder in subFolders:
            handlerFolder(folderName, subFolder)
        for fname in fileNames:
            handlerFile(folderName, fname)

class ZipWriter:
    def __init__(self, base, zipObj):
        self._base = base
        self._zipObj = zipObj

    def writeFolder(self, folderName, subFolder):
        print "INFO: writeFolder folderName {0} subFolder {1}".format(folderName, subFolder)
        original = os.path.join(folderName, subFolder)
        target = self._getTarget(folderName, subFolder)
        self._zipObj.write(original, target)

    def writeFile(self, folderName, fname):
        print "INFO: writeFile folderName {0} fname {1}".format(folderName, fname)
        original = os.path.join(folderName, fname)
        target = self._getTarget(folderName, fname)
        with open(original, 'rb') as fileToInclude:
            content = fileToInclude.read()
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
        self._zipObj.writestr(target, content)

    def _getTarget(self, folderName, item):
        subDirInZip = os.path.relpath(folderName, self._base)
        target = os.path.join(subDirInZip, item)
        print "INFO: target {0}".format(target)
        return target

def createDownloadZip(target, sourceDir):
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
        walkDirectory(sourceDir, \
            lambda folderName, subFolder: zipWriter.writeFolder(folderName, subFolder), \
            lambda folderName, fname: zipWriter.writeFile(folderName, fname))

def createDownloadZipFromLine(line):
    source = line
    target = os.path.join(targetDir, os.path.basename(source) + ".zip")
    createDownloadZip(target, source)

def handleLine(line):
    line = line.strip()
    if len(line) == 0:
        return
    if line[0] == "#":
        return
    createDownloadZipFromLine(line)

def createAllDownloadZips(descriptorFile):
    walkLines(descriptorFile, handleLine)

if not os.path.exists(targetDir):
    os.makedirs(targetDir)
createAllDownloadZips(downloadsDescriptor)

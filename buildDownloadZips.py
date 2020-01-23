#!/usr/bin/python
#
# Please run this script from your checkout directory of
# ibis4manual.
#
# This script is needed to build the manual for the Frank!framework.
# Within the manual code we want download links to Frank code that
# complements the explanations in the text.
#
# This script reads a file "buildDownloadZips.txt". This
# file lists all subdirectories of ibis4manual that need
# to be zipped. Optionally, you can add a target file name
# (no directory, omit the .zip extension).
#
# Only files tracked with git are added to the
# zips. These zips appear in directory
# "docs/source/downloads".
#
# Why do we only add tracked files to the download zips? As
# an example, consider ibisdoc.xsd, the XML schema that
# defines the grammar of the Frank language. This file
# is typically downloaded from the Frank!Framework. Users
# of the manual are advised to download ibisdoc.xsd
# from there. Therefore, the download zips should not contain
# ibisdoc.xsd.
#
# On the other hand, ibisdoc.xsd is useful for editors
# of this ibis4manual project, because they want
# support when they edit Frank config. Therefore,
# ibisdoc.xsd appears in the checkout. The solution
# is to add ibisdoc.xsd to .gitignore and to omit
# ignored files from download zips.
#
import os
import sys
import subprocess
from zipfile import ZipFile

targetDir = os.path.normpath("docs/source/downloads")
downloadsDescriptor = "buildDownloadZips.txt"

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
        if subDirInZip == "." :
            target = item
        else :
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
        walkTrackedFilesInDirectory(sourceDir, \
            lambda folderName, fname: zipWriter.writeFile(folderName, fname))

def createDownloadZipFromLine(line):
    words = line.strip().split()
    if len(words) == 1:
        source = words[0]
        targetBase = os.path.basename(source)
    elif len(words) == 2:
        source = words[0]
        targetBase = words[1]
    else:
        print "ERROR: Invalid line: " + line
    target = os.path.join(targetDir, targetBase + ".zip")
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

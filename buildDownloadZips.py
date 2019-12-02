#!/usr/bin/python

# This script is needed to build the manual for the Frank!framework.
# Within the manual code we want download links to Frank code that
# complements the explanations in the text. This script produces
# these zip files from the subdirectories of the src directory.
#
# This script reads a file "buildZips.txt". This
# file lists all subdirectories of ibis4manual that need
# to be zipped. These zips appear in directory
# "docs/source/downloads".

import os
import sys
from zipfile import ZipFile

targetDir = os.path.normpath("docs/source/downloads")
downloadsDescriptor = "buildZips.txt"

def walkLines(fname, handler):
    with open(fname, "r") as f:
        for cnt, line in enumerate(f):
            handler(line)

def walkDirectory(theDirectory, handler):
    for folderName, subFolders, fileNames in os.walk(theDirectory):
        for fname in fileNames:
            handler(folderName, fname)

def stripParentPath(base, folderName, fname):
    baseInZip = os.path.basename(base)
    subDirInZip = os.path.relpath(folderName, base)
    return os.path.join(baseInZip, subDirInZip, fname)

class ZipWriter:
    def __init__(self, base, zipObj):
        self._base = base
        self._zipObj = zipObj
    def write(self, folderName, fname):
        original = os.path.join(folderName, fname)
        target = stripParentPath(self._base, folderName, fname)
        self._zipObj.write(original, target)

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
    print "Creating downloadable file {0} from directory {1}".format(target, sourceDir)
    with ZipFile(target, "w") as z:
        zipWriter = ZipWriter(sourceDir, z)
        walkDirectory(sourceDir, lambda folderName, fname: zipWriter.write(folderName, fname))

def createDownloadZipFromLine(line):
    source = line.strip()
    target = os.path.join(targetDir, os.path.basename(source) + ".zip")
    createDownloadZip(target, source)

def createAllDownloadZips(descriptorFile):
    walkLines(descriptorFile, createDownloadZipFromLine)

if not os.path.exists(targetDir):
    os.makedirs(targetDir)
createAllDownloadZips(downloadsDescriptor)


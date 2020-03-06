#!/usr/bin/python
#
# Please run this script from your checkout directory of
# the Frank!Runner.
#
# This script is needed to build the manual for the Frank!Framework.
# It does two things:
#
# i)
# The manual presents snippets of XML and property file data. These
# snippets guide the student to build a working Frank config. All
# the versions that the student creates while doing the tutorial
# are in this Git repository. This script generates the snippets to
# include from these files.
#
# ii)
# Within the manual code we want download links to Frank code that
# complements the explanations in the text. This script produces
# these zip files from the subdirectories of the src directory.
#
# The produced zips appear in download links within the manual.
# ReadTheDocs thus needs access to the .zip files during its build.
# Please run this script before executing the ReadTheDocs build.
#
# This script reads a file "buildDownloadZips.txt". This
# file lists all subdirectories of ibis4manual that need
# to be zipped. Only files tracked with git are added to the
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
# support when they edit Frank code. Therefore,
# ibisdoc.xsd appears in the checkout. The solution
# is to add ibisdoc.xsd to .gitignore and to omit
# ignored files from download zips.
#
from buildDownloadZips import createAllDownloadZips
from createSnippets import createAllSnippets
from createSnippets import META_YML

import os

downloadZipsDir = "docs/source/downloads"
downloadsDescriptor = "buildDownloadZips.txt"
tutorialStepsDir = "srcSteps"
snippetsDir = "docs/source/snippets"

createAllDownloadZips(downloadsDescriptor, downloadZipsDir, set([META_YML]))
createAllSnippets(tutorialStepsDir, snippetsDir)
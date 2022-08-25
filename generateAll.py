#!/usr/bin/python
#
# Please run this script from your checkout directory of
# the Frank!Runner. See CONTRIBUTING.md for details on what it does.
#
# This script is needed to build the manual for the Frank!Framework.
# It does two things:
#
# i)
# Run TutorialSteps. See the comments in createAllSnippets.py for details.
#
# ii)
# Build download zips. See the comments in file "buildDownloadZips.py"
# for details.
#
# Please run this script before doing the Sphinx build. Sphinx
# needs the output produced by this script.
#

# These lines are needed if Python has not been installed with an installer.
import sys
sys.path.append(".")

from buildDownloadZips import createAllDownloadZips
from createSnippets import createAllSnippets
from createSnippets import META_YML

import os

# Directory where generated download zips are stored.
downloadZipsDir = "docs/source/downloads"

# Configuration file that specifies what to zip.
downloadsDescriptor = "buildDownloadZips.txt"

# Root directory for all version histories of all
# Frank configs
tutorialStepsDir = "srcSteps"

# Output directory in which generated reStructuredText snippets
# are stored.
snippetsDir = "docs/source/snippets"

IBISDOC_XSD = "ibisdoc.xsd"
FRANK_CONFIG_XSD = "FrankConfig.xsd"

hasErrors = createAllDownloadZips(downloadsDescriptor, downloadZipsDir, set([META_YML, IBISDOC_XSD, FRANK_CONFIG_XSD]))
if not hasErrors:
    createAllSnippets(tutorialStepsDir, snippetsDir, [IBISDOC_XSD, FRANK_CONFIG_XSD])
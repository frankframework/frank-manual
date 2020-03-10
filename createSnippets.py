import os
import TutorialSteps
from fileUtils import makeDirectoryIfNotPresent

META_YML = "meta.yml"

def handlerAddOld(comparison, relPath, lines):
    if relPath != META_YML:
        comparison.addOld(TutorialSteps.RelPath(relPath.split("/")), lines)
def handlerAddNew(comparison, relPath, lines):
    if relPath != META_YML:
        comparison.addNew(TutorialSteps.RelPath(relPath.split("/")), lines)

def createStepSnippets(configName, stepName, oldDir, newDir, snippetsDir):
    """
    Handle two consecutive versions, say the previous and the current, of a Frank config.
    
        Parameters:
            configName: The name of the Frank!Config.
            stepName: The name of the current version.
            oldDir: Object of type GitDirectoryTree as defined in gitDirectoryTree.py.
                Holds the root directory of the previous version.
            newDir: Object of type GitDirectoryTree. Holds the root directory
                of the current version.
    
    This member function does the following:
    - Parse meta.yml of the current version into a list of FileDifference object.
      Class FileDifference is defined in treeCompare.py.
    - Create a TreeComparison object from this list.
    - Feed the TreeComparison with the files of the previous version. Only add
      files under version control and omit meta.yml.
    - Feed the TreeComparison with the files of the current version. Only add
      files under version control and omit meta.yml.
    - Run the TreeComparison to get check the claims of meta.yml
      and generate the snippets.
    - Write the snippets to disk. Each snippet is written to a file
      configName/stepName/snippetName.txt (not .rst because that would
      produce warnings from Sphinx).
    """
    print "Doing Frank config {0} step {1}".format(configName, stepName)
    hasErrors = False
    with newDir.openFile(META_YML) as f:
        diffs, error = expectedDifferences = TutorialSteps.createFileDifferences(f)
    if error is not None:
        raise Exception("Did not understand meta.yml for config {0} and step {1}".format(configName, stepName))
    compare = TutorialSteps.TreeComparison(diffs)
    if oldDir is not None:
        oldDir.browse(lambda relPath, lines: handlerAddOld(compare, relPath, lines))
    newDir.browse(lambda relPath, lines: handlerAddNew(compare, relPath, lines))
    snippets, errors = compare.run()
    if errors is not None:
        for error in errors:
            hasErrors = True
            print "ERROR: " + error
    for snippet in snippets:
        makeDirectoryIfNotPresent("/".join([configName, stepName]), os.path.abspath(snippetsDir))
        outputFileName = os.path.join(os.path.abspath(snippetsDir), configName, stepName, snippet.getName() + ".txt")
        with open(outputFileName, "w") as f:
            for line in snippet.getLines():
                f.write(line + "\n")
    return hasErrors

def createFrankConfigSnippets(configRoot, snippetsDir):
    name = configRoot.getLastComponent()
    stepDirs = configRoot.getSubdirs()
    hasErrors = False
    if len(stepDirs) >= 1:
        hasErrors = createStepSnippets(name, stepDirs[0].getLastComponent(), None, stepDirs[0], snippetsDir)
    for stepIdx in range(1, len(stepDirs)):
        stepName = stepDirs[stepIdx].getLastComponent()
        hasErrors = hasErrors or createStepSnippets(name, stepName, stepDirs[stepIdx-1], stepDirs[stepIdx], snippetsDir)
    return hasErrors

def createAllSnippets(tutorialStepsDir, snippetsDir):
    """
Run TutorialSteps.

    Arguments:
        tutorialStepsDir: Root directory for all Frank configurations
            and all versions to process. These are the input files.
        snippetsDir: Root directory for all generated reStructuredText
            snippets.

TutorialSteps expects a directory tree like the following:

tutorialStepsDir
|- FrankConfig1
   |- v01
      |- meta.yml
      |- Configuration.xml
      |- ...
   |- v02
      |- meta.yml
      |- Configuration.xml
      |- ...
   |- ...

TutorialSteps will process the subdirectories of a Frank config
directory in alphabetical order. For example, FrankConfig1/v01
is processed before FrankConfig1/v02. Each file meta.yml contains
YAML code that specifies what differences with the previous version
are expected. In the first version, meta.yml is also relevant and
gives the expected differences relative to the empty folder, typically
adds. TutorialSteps checks whether the actual differences between
versions agree with the meta.yml files.

When checking the actual differences between two consecutive versions,
only files checked in to Git are considered. This is useful, because
it allows file ibisdoc.xsd to be ignored. In addition, the meta.yml
files are excluded from the comparison.

You can use directories with a meta.yml to generate download zips. The
meta.yml files will automatically be omitted from the zips.

For the format of the meta.yml files, see the unit test in
TutorialSteps/compareFactory.py. For a general introduction to
YAML see wikipedia, https://en.wikipedia.org/wiki/YAML. A YAML
defines a nested structure of lists, dictionaries and scalars.

The top-level structure of each meta.yml is a list of dictionaries,
each having one key. This key is "snippet" or "file".

A "snippet" item defines an reStructuredText snippet produce and gives
it a name. The value of the "snippet" key is itself a dictionary. The
following keys are supported: "name", "markup" and "context". They
have the following meaning:

    - name: The name, use this to reference a snippet in a "file" item.
    - markup: The markup language (none or XML). Use this to manage syntax
      highlighting in the Frank!Manual.
    - context: A snippet originates from a difference between some file
      in the previous version to the corresponding file in the current version.
      The snippet will be the changed lines according to the current version and
      include additional lines around it that are not different. This property
      defines the number of additional unchanged lines to add before and after
      the difference.

For a "file" item, the value of the "file" key is itself a dictionary with
two keys:

    - path: The considered path, relative to the root directory
        of the version.
    - change: Definition of the change. There are three possibilities
        for the value, namely the scalar "add", the scalar "del" or
        a list of changes. The latter defines that the path is present both
        in the previous and the current version but that they are different.
        There can be multiple differences.

Each difference within a file change list is a dictionary that can have the
following keys:

    - insert: The number of inserted lines.
    - old: The number of lines within a consecutive block being replaced.
    - new: The number of lines that replace the block.
    - snippet: References the snippet to generate from the difference.
    - highlight: Optional. If defined, the generate snippet will include
      a directive to highlight the changed lines.

A file change dictionary either has key "insert" and not "old" and "new",
or it does not have "insert" and does have "old" and "new".

A file that differs from its previous version can have multiple
differences. Each difference is about a consecutive block of lines
that is replaces by another block of lines. Different changes of
the same file can reference the same snippet. If you do this,
TutorialSteps checks whether the differences become adjacent of
oerlapping after addig the defined number of context lines. If so,
the differences are merged before generating the reStructuredText.
If not, an error is generated. This error reminds you that you have
to update the manual text.

When you have multiple differences and reference different snippets,
the TutorialSteps checks that the snippets do not become adjacent or
overlapping when adding the context lines. If the snippets become
adjacent or overlapping, an error is produced. You have to change the
manual or you need another intermediate version.
"""
    makeDirectoryIfNotPresent(snippetsDir)
    tutorialStepsRoot = TutorialSteps.GitDirectoryTree(tutorialStepsDir)
    hasErrors = False
    for frankConfigDir in tutorialStepsRoot.getSubdirs():
        hasErrors = hasErrors or createFrankConfigSnippets(frankConfigDir, snippetsDir)
    if hasErrors:
        print("*** ERRORS CHECKING srcSteps AND GENERATING SNIPPETS")

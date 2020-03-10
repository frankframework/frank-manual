import os
from fileUtils import makeDirectoryIfNotPresent
import TutorialSteps
from TutorialSteps import META_YML

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
            snippetsDir: Root directories for storing snippets.

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
    print "Doing Frank config {0} step {1}, predecessor {2}".format(configName, stepName, \
        oldDir.getLastComponent() if oldDir is not None else "<none>")
    hasErrors = False
    if not newDir.fileExists(META_YML):
        print "ERROR: No file {0} present.".format(META_YML)
        hasErrors = True
        return hasErrors
    with newDir.openFile(META_YML) as f:
        diffs, dummyPredecessor, error = TutorialSteps.createFileDifferences(f)
    if error is not None:
        print "ERROR: Did not understand meta.yml for config {0} and step {1}, error is {2}".format(configName, stepName, error)
        hasErrors = True
        return hasErrors
    compare = TutorialSteps.TreeComparison(diffs)
    if oldDir is not None:
        oldDir.browse(lambda relPath, lines: handlerAddOld(compare, relPath, lines))
    newDir.browse(lambda relPath, lines: handlerAddNew(compare, relPath, lines))
    snippets, errors = compare.run()
    if errors is not None:
        for error in errors:
            hasErrors = True
            print "ERROR: " + error
    if snippets is None:
        hasErrors = True
    else:
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
    print "INFO: Step dirs are: {0}".format(", ".join([item.getLastComponent() for item in stepDirs]))
    hasErrors = False
    steps, error = TutorialSteps.sortDirectories(stepDirs)
    if error is not None:
        print "ERROR: configuration {0} while getting predecessor graph: {1}".format(name, error)
        return True
    for step in steps:
        stepName = step.getNew().getLastComponent()
        hasErrors = createStepSnippets(name, stepName, step.getOld(), step.getNew(), snippetsDir) or hasErrors
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
each having one key. This key is "predecessor", "snippet" or "file".

A "predecessor" key can be used to define another reference directory
for this step. The default is the previous directory according to the
alphabetical sort order. The value of this key should be a string when
defined. This feature is useful for explaining optional changes to a
configuration, which are not relevant for the remainder of your story.

A "snippet" item defines a reStructuredText snippet to produce and gives
it a name. The value of the "snippet" key is itself a dictionary. The
following keys are supported: "name", "markup", "context", "before"
and "after". They have the following meaning:

    - name: The name, use this to reference a snippet in a "file" item.
    - markup: The markup language (none or XML). Use this to manage syntax
      highlighting in the Frank!Manual.
    - context: A snippet originates from a difference between some file
      in the previous version to the corresponding file in the current version.
      The snippet will be the changed lines according to the current version and
      include additional lines around it that are not different. This property
      defines the number of additional unchanged lines to add before and after
      the difference.
    - before: Like context, but lines are only added before the change.
    - after: Like context, but lines are only added after the change.

Note, either use "context" and not "before" or "after", or omit "context"
and use both "before" and "after".

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

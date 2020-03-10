import os
import subprocess

class GitDirectoryTree:
    def __init__(self, relPath, base=os.getcwd()):
        if not type(relPath) is str:
            raise TypeError("relPath should be string")
        if len(relPath) == 0:
            raise ValueError("relPath should not be empty string")
        if "\\" in relPath:
            raise ValueError("Expect unix-style relPath argument")
        self._lastPathComponent = relPath.split("/")[-1]
        self._absPath = os.path.join(base, relPath)
        if not os.path.isdir(self._absPath):
            raise ValueError("Path is not a directory")
    def getLastComponent(self):
        return self._lastPathComponent
    def getSubdirs(self):
        fileAndDirSet = set([])
        self._browsePaths(lambda p: fileAndDirSet.add(p.split("/")[0]))
        subdirsSet = {item for item in fileAndDirSet if os.path.isdir(os.path.join(self._absPath, item))}
        subdirsSortedList = sorted(list(subdirsSet))

        return [GitDirectoryTree(item, self._absPath) for item in subdirsSortedList]
    def _browsePaths(self, handler):
        cmd = "git ls-files {0}".format(self._absPath)
        trackedFiles = subprocess.check_output(cmd, shell=True, cwd=self._absPath).splitlines()
        for relPath in trackedFiles:
            handler(relPath)
    def browse(self, handler):
        self._browsePaths(lambda relPath: self._handleBrowsePath(relPath, handler))
    def _handleBrowsePath(self, relPath, handler):
        toOpen = os.path.join(self._absPath, relPath)
        with open(toOpen, "r") as f:
            rawLines = f.readlines()
            lines = [line.replace("\r\n", "\n").rstrip() for line in rawLines]
        handler(relPath, lines)
    def fileExists(self, path):
        return os.path.isfile(os.path.join(self._absPath, path))
    def openFile(self, path):
        return open(os.path.join(self._absPath, path))
    def getSubdirIfPresent(self, subdir):
        subdirsDict = {d.getLastComponent(): d for d in self.getSubdirs()}
        if subdir in subdirsDict:
            return subdirsDict[subdir]
        else:
            return None

if __name__ == "__main__":

    import unittest

    class TestGitDirectoryTree(unittest.TestCase):
        def test_get_correct_subdir_names(self):
            instance = GitDirectoryTree("testdata")
            subDirs = instance.getSubdirs()
            self.assertEquals(len(subDirs), 2)
            self.assertEquals("dir1", subDirs[0].getLastComponent())
            self.assertEquals("dir2", subDirs[1].getLastComponent())
        def test_browse_gives_correct_relpaths_and_line_lists(self):
            expected = sorted("""f1.txt: f1 line 0
f1.txt: f1 line 1
dir1/f1.txt: dir1/f1 line 0
dir1/f1.txt: dir1/f1 line 1
dir2/f1.txt: dir2/f1 line 0
dir2/f1.txt: dir2/f1 line 1
dir2/f1.txt: dir2/f1 line 2""".replace("\r\n", "\n").split("\n"))
            instance = GitDirectoryTree("testdata")
            actual = []
            instance.browse(lambda relPath, lines: actual.extend([relPath + ": " + line for line in lines]))
            actual.sort()
            self.assertEquals(actual, expected)
        def test_if_subdir_present_then_returned(self):
            instance = GitDirectoryTree("testdata")
            subDir = instance.getSubdirIfPresent("dir1")
            self.assertIsNotNone(subDir)
            self.assertTrue(isinstance(subDir, GitDirectoryTree))
            self.assertEquals(subDir.getLastComponent(), "dir1")
        def test_if_subdir_not_present_then_none_returned(self):
            instance = GitDirectoryTree("testdata")
            subDir = instance.getSubdirIfPresent("nonExistingDir")
            self.assertIsNone(subDir)
        def test_file_exists(self):
            instance = GitDirectoryTree("testdata")
            self.assertTrue(instance.fileExists("f1.txt"))
            self.assertFalse(instance.fileExists("doesNotExist.txt"))
        def test_open_file(self):
            instance = GitDirectoryTree("testdata")
            with instance.openFile("f1.txt") as f:
                actualLines = [line.replace("\r\n", "\n").rstrip() for line in f.readlines()]
            expectedLines = ["f1 line 0", "f1 line 1"]
            self.assertEquals(actualLines, expectedLines)

    unittest.main()

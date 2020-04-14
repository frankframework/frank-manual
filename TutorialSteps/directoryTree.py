import os
import subprocess

class DirectoryTree:
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
            raise ValueError("Path is not a directory: " + self._absPath)
    def getLastComponent(self):
        return self._lastPathComponent
    def getSubdirs(self):
        fileAndDirSet = set([])
        self._browsePaths(lambda p: fileAndDirSet.add(p.split("/")[0]))
        subdirsSet = {item for item in fileAndDirSet if os.path.isdir(os.path.join(self._absPath, item))}
        subdirsSortedList = sorted(list(subdirsSet))

        return [DirectoryTree(item, self._absPath) for item in subdirsSortedList]
    def _browsePaths(self, handler):
        for dirname, _, filenames in os.walk(self._absPath):
            for filename in filenames:
                absPath = os.path.join(dirname, filename)
                relPath = os.path.relpath(absPath, self._absPath)
                relPath = relPath.replace(os.sep, "/")
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

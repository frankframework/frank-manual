# Directory utils. If you run this from the command line, you test
# creating a directory if it does not exist. You can also import
# this file and use its makeDirectoryIfNotPresent function.

import os

def makeDirectoryIfNotPresent(linuxStyleRelativePath, parent=os.getcwd()):
    if not type(linuxStyleRelativePath) is str:
        raise TypeError("String expected")
    if linuxStyleRelativePath == "":
        raise ValueError("Path should not be empty")
    if "\\" in linuxStyleRelativePath:
        raise ValueError("Path is not Linux-style")
    if linuxStyleRelativePath != linuxStyleRelativePath.strip():
        raise ValueError("Path is not stripped")
    if linuxStyleRelativePath[0] == "/":
        raise ValueError("Path is not relative")
    if "." in linuxStyleRelativePath:
        raise ValueError("Paths with . or .. not supported")
    curPath = parent
    for component in linuxStyleRelativePath.split("/"):
        curPath = os.path.join(curPath, component)
        if not os.path.exists(curPath):
            os.mkdir(curPath)

if __name__ == "__main__":

    import sys

    dirToCreate = sys.argv[1]
    makeDirectoryIfNotPresent(dirToCreate)

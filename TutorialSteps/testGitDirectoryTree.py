from .gitDirectoryTree import *

if __name__ == "__main__":

    import unittest

    class TestGitDirectoryTree(unittest.TestCase):
        def test_get_correct_subdir_names(self):
            instance = GitDirectoryTree("TutorialSteps/testdata")
            subDirs = instance.getSubdirs()
            self.assertEqual(len(subDirs), 2)
            self.assertEqual("dir1", subDirs[0].getLastComponent())
            self.assertEqual("dir2", subDirs[1].getLastComponent())
        def test_browse_gives_correct_relpaths_and_line_lists(self):
            expected = sorted("""f1.txt: f1 line 0
f1.txt: f1 line 1
dir1/f1.txt: dir1/f1 line 0
dir1/f1.txt: dir1/f1 line 1
dir2/f1.txt: dir2/f1 line 0
dir2/f1.txt: dir2/f1 line 1
dir2/f1.txt: dir2/f1 line 2""".replace("\r\n", "\n").split("\n"))
            instance = GitDirectoryTree("TutorialSteps/testdata")
            actual = []
            instance.browse(lambda relPath, lines: actual.extend([relPath + ": " + line for line in lines]))
            actual.sort()
            self.assertEqual(actual, expected)
        def test_if_subdir_present_then_returned(self):
            instance = GitDirectoryTree("TutorialSteps/testdata")
            subDir = instance.getSubdirIfPresent("dir1")
            self.assertIsNotNone(subDir)
            self.assertTrue(isinstance(subDir, GitDirectoryTree))
            self.assertEqual(subDir.getLastComponent(), "dir1")
        def test_if_subdir_not_present_then_none_returned(self):
            instance = GitDirectoryTree("TutorialSteps/testdata")
            subDir = instance.getSubdirIfPresent("nonExistingDir")
            self.assertIsNone(subDir)
        def test_file_exists(self):
            instance = GitDirectoryTree("TutorialSteps/testdata")
            self.assertTrue(instance.fileExists("f1.txt"))
            self.assertFalse(instance.fileExists("doesNotExist.txt"))
        def test_open_file(self):
            instance = GitDirectoryTree("TutorialSteps/testdata")
            with instance.openFile("f1.txt") as f:
                actualLines = [line.replace("\r\n", "\n").rstrip() for line in f.readlines()]
            expectedLines = ["f1 line 0", "f1 line 1"]
            self.assertEqual(actualLines, expectedLines)

    unittest.main()

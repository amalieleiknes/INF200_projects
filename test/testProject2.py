import Project_2.showLines
import unittest


class testProject2(unittest.TestCase):
    def testLineNumbers(self):
        fromFile = Project_2.showLines.head('../Project_2/sample', 5)
        print(fromFile)
        fasit = "test"
        self.assertEqual(fromFile, fasit, "ERROR")


if __name__ == '__main__':
    unittest.main()

import unittest
from repositorycommitcount import repoCount


class testRepoCount(unittest.TestCase):

    def testRepoCount(self):
        self.assertIsInstance(repoCount('richkempinski'), dict)
        self.assertIsInstance(repoCount('bshinn01'), dict)

    def testIncorrectOutputs(self):
        self.assertIsInstance(repoCount('###'), int)
        self.assertIsInstance(repoCount(''), int)


if __name__ == '__main__':
    unittest.main()

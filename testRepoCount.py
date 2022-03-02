import unittest
from repositorycommitcount import repoCount
from unittest.mock import MagicMock
from unittest.mock import patch
import requests
import json


class testRepoCount(unittest.TestCase):

    def testRepoCount(self):
        self.assertIsInstance(repoCount('richkempinski'), dict)
        self.assertIsInstance(repoCount('bshinn01'), dict)

    def testIncorrectOutputs(self):
        self.assertIsInstance(repoCount('###'), int)
        self.assertIsInstance(repoCount(''), int)


if __name__ == '__main__':
    unittest.main()

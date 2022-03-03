import unittest
from repositorycommitcount import repoCount
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import patch
import requests
import json

mock_ref = {
    'https://api.github.com/users/bshinn01/repos':
    'json_files/bshinn01_repos.json',

    'https://api.github.com/repos/bshinn01/Data-Structures-Endterm-Project/commits':
    'json_files/Data-Structures-Endterm-Project.json',

    'https://api.github.com/repos/bshinn01/Classify_Triangle/commits':
    'json_files/Classify_Triangle.json',

    'https://api.github.com/repos/bshinn01/Anagrams-Assignment/commits':
    'json_files/Anagrams-Assignment.json'
}


class FakeResponse:
    def __init__(self, json_data):
        self.json_data = json_data
        self.status_code = requests.codes.ok

    def json(self):
        return self.json_data


def mocked_requests_get(*args):
    if args[0] in mock_ref:
        with open(mock_ref[args[0]]) as f:
            return FakeResponse(json.load(f))
    return FakeResponse(None)


class testRepoCount(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def testType(self, mock_get):
        self.assertIsInstance(repoCount('bshinn01'), dict)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def testOutput(self, mock_get):
        self.assertEqual(repoCount('bshinn01'), {'Anagrams-Assignment': 3,
                                                 'Classify_Triangle': 7,
                                                 'Data-Structures-Endterm-Project': 2})


if __name__ == '__main__':
    unittest.main()

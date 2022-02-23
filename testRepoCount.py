import unittest
from repositorycommitcount import repoCount


class testRepoCount(unittest.TestCase):

    def testRepoCount(self):
        output = repoCount('richkempinski')
        if type(output) == int or type(output) is None:
            print('Exceeded limit')
            return "Exceeded limit"

        self.assertEqual(output, output.update({'hellogitworld': 30}))

        self.assertEqual(output, output.update({'helloworld': 6}))

    def testIncorrectOutputs(self):
        self.assertIsInstance(repoCount('###'), int)


if __name__ == '__main__':
    unittest.main()

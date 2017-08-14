import fileinput
import unittest


class TestFileRead(unittest.TestCase):
    def test_inputoutput(self):
        eko_json = open('autocomplete.json', 'r')
        result = fileinput.transform(eko_json)
        expected_result = ["on\tEko InterludePlayer Method", "on"]
        self.maxDiff = None
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

import fileinput
import unittest
import json
import urllib.request


class TestFileRead(unittest.TestCase):
    def test_inputoutput(self):
        with urllib.request.urlopen(
            "https://developer.helloeko.com/api/autocomplete.json")\
                as url:
            data = json.loads(url.read().decode())
        result = fileinput.transform(data)
        expected_result = ["on\tEko InterludePlayer Method", "on"]
        self.maxDiff = None
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

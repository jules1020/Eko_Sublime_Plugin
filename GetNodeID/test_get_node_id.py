import get_node_id
import unittest
from pathlib import Path


class TestGetNodeID(unittest.TestCase):
    def test_iteratefolders(self):
        directory = Path('.')
        result = get_node_id.search(directory)
        expected_result = 'node_beginning_39j7h2'
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

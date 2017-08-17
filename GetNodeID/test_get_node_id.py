"""Import get_node_id, unittest, and Path from pathlib."""
import get_node_id
import unittest
import pathlib


class TestGetNodeID(unittest.TestCase):
    """Class test for searching of node ids in eko project directory tree."""

    def test_iteratefolders(self):
        """Function to test directory iteration."""
        directory = pathlib.Path('.')
        result = get_node_id.search(directory)
        expected_result = ["node_beginning_39j7h2", "node_julian_j391jg"]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

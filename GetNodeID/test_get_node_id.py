import get_node_id
import unittest


class TestGetNodeID(unittest.TestCase):
    def test_iteratefolders(self):
        directory = Path('.')
        result = get_node_id.search(directory)
        expected_result = 'nodes/'
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

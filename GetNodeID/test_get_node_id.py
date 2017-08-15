import get_node_id
import unittest


class TestGetNodeID(unittest.TestCase):
    def test_locatefolder(self):
        path = 'path/to/folder'
        result = get_node_id.search(path)
        expected_result = '__eko__'
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

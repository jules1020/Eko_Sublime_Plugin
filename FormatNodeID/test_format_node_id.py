"""Import unittest."""
import unittest
import format_node_id


class TestFormatNodeID(unittest.TestCase):
    """Class for testing the formating of node ids."""

    def test_formatnodeids(self):
        """Function to test formating."""
        node_ids = ["node_beginning_39j7h2", "node_julian_j391jg"]
        result = format_node_id.transform_nodeid(node_ids)
        expected_result = [
            ["node_beginning_39j7h2\tProject Node", "node_beginning_39j7h2"],
            ["node_julian_j391jg\tProject Node", "node_julian_j391jg"]]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

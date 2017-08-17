"""Import unittest."""
import unittest
import format_node_id


class TestFormatNodeID(unittest.TestCase):
    """Class for testing the formating of node ids."""

    def test_formatnodeids(self):
        """Function to test formating."""
        node_ids = ['node_beginning_39j7h2', 'node_julian_j391jg']
        result = format_node_id.format(node_ids)
        expected_result = 

if __name__ == "__main__":
    unittest.main()

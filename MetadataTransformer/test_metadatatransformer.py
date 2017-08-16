"""Importing metadatatransformer.py and unittest for testing."""
import metadatatransformer
import unittest


class TestMetadataTransformer(unittest.TestCase):
    """Class for testing MetadataTransformer."""

    def test_objects(self):
        """Function to test correct object transform."""
        objects = [
            {"name": "on", "memberof": "InterludePlayer", "kind": "function"},
            {"name": "update", "memberof": "Repository", "kind": "function"},
            {"name": "pluginInited", "memberof": "InterludePlayer",
                "kind": "function"},
            {"name": "once", "memberof": "Node", "kind": "function"},
            {"name": "trigger", "memberof": "Node", "kind": "function"},
            {"name": "version", "memberof": "InterludePlayer",
                "kind": "member"},
            {"name": "open", "memberof": "urls", "kind": "function"}]
        result = metadatatransformer.transform(objects)
        expected_result = [
            ["on\tEko InterludePlayer Method", "on"],
            ["update\tEko Repository Method", "update"],
            ["pluginInited\tEko InterludePlayer Method", "pluginInited"],
            ["once\tEko Node Method", "once"],
            ["trigger\tEko Node Method", "trigger"],
            ["version\tEko InterludePlayer Member", "version"],
            ["open\tEko urls Method", "open"]]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

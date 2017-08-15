import metadatatransformer
import unittest


class TestMetadataTransformer(unittest.TestCase):
    def test_objects(self):
        objects = [
            {"name": "on", "memberof": "InterludePlayer", "kind": "function"},
            {"name": "update", "memberof": "Repository", "kind": "function"},
            {"name": "pluginInited", "memberof": "InterludePlayer",
                "kind": "function"},
            {"name": "once", "memberof": "Node", "kind": "function"},
            {"name": "trigger", "memberof": "Node", "kind": "function"},
            {"name": "version", "memberof": "InterludePlayer",
                "kind": "member"}]
        result = metadatatransformer.transform(objects)
        expected_result = [
            ["on\tEko InterludePlayer Method", "on"],
            ["update\tEko Repository Method", "update"],
            ["pluginInited\tEko InterludePlayer Method", "pluginInited"],
            ["once\tEko Node Method", "once"],
            ["trigger\tEko Node Method", "trigger"],
            ["version\tEko InterludePlayer Member", "version"]]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

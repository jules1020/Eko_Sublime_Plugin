import metadatatransformer
import unittest


class TestMetadataTransformer(unittest.TestCase):
    def test_objects(self):
        objects = [
            {"name": "on", "memberof": "InterludePlayer"},
            {"name": "update", "memberof": "Repository"},
            {"name": "pluginInited", "memberof": "InterludePlayer"},
            {"name": "once", "memberof": "Node"},
            {"name": "trigger", "memberof": "Node"}]
        result = metadatatransformer.transform(objects)
        expected_result = [
            ["on\tEko InterludePlayer Method", "on"],
            ["update\tEko Repository Method", "update"],
            ["pluginInited\tEko InterludePlayer Method", "pluginInited"],
            ["once\tEko Node Method", "once"],
            ["trigger\tEko Node Method", "trigger"]]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

import metadatatransformer
import unittest


class TestMetadataTransformer(unittest.TestCase):
    # def test_objectwithname(self):
    #     """OK"""
    #     objectwithlongname = {"name": "isFullscreenSupported"}
    #     result = metadatatransformer.transform(objectwithlongname)
    #     expected_result = ["isFullscreenSupported", "isFullscreenSupported"]
    #     self.assertEqual(result, expected_result)

    def test_3objects(self):
        objects = [
            {"name": "on"},
            {"name": "update"},
            {"name": "pluginInited"}]
        result = metadatatransformer.transform(objects)
        expected_result = [["on", "on"], ["update", "update"], ["pluginInited", "pluginInited"]]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

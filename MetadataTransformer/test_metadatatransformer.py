import metadatatransformer
import unittest

class TestMetadataTransformer(unittest.TestCase):
    def test_objectwithname(self):
        objectwithlongname = {"name": "isFullscreenSupported"}
        result = metadatatransformer.transform(objectwithlongname)
        expected_result = ["isFullscreenSupported", "isFullscreenSupported"]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

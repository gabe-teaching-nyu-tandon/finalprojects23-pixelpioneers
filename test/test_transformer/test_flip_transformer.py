import unittest
import cv2
import numpy as np
from pixelpioneers.exceptions import ImageTransformationError
from pixelpioneers.actions.transformers import FlipTransformer

class FlipTransformerTests(unittest.TestCase):
    def setUp(self):
        self.transformer = FlipTransformer("horizontal")
        self.image = np.zeros((100, 100, 3), dtype=np.uint8)  # Create a dummy image

    def test_flip_horizontal(self):
        transformed_image = self.transformer.apply(self.image)
        expected_image = cv2.flip(self.image, 1)
        np.testing.assert_array_equal(transformed_image, expected_image)

    def test_flip_vertical(self):
        self.transformer.mode = "vertical"
        transformed_image = self.transformer.apply(self.image)
        expected_image = cv2.flip(self.image, 0)
        np.testing.assert_array_equal(transformed_image, expected_image)

    def test_none_image(self):
        with self.assertRaises(ImageTransformationError):
            self.transformer.apply(None)

if __name__ == "__main__":
    unittest.main()

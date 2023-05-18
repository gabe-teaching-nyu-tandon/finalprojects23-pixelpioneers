import unittest
import cv2
import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError
from pixelpioneers.actions.transformers import RotateTransformer


class RotateTransformerTest(unittest.TestCase):

    def setUp(self):
        self.transformer = RotateTransformer(angle=45)

    def test_apply_with_valid_image(self):
        # Create a test image
        image = np.zeros((100, 100, 3), dtype=np.uint8)

        # Apply rotation
        rotated_image = self.transformer.apply(image)

        # Assert the output is not None and has the same shape as the input image
        self.assertIsNotNone(rotated_image)
        self.assertEqual(rotated_image.shape, image.shape)

    def test_apply_with_none_image(self):
        # Assert that applying transformation with None image raises an ImageTransformationError
        with self.assertRaises(ImageTransformationError):
            self.transformer.apply(None)

if __name__ == '__main__':
    unittest.main()

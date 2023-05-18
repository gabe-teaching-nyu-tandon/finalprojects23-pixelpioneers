import unittest
import cv2
import numpy as np

from pixelpioneers.exceptions import ImageTransformationError
from pixelpioneers.actions.transformers import ResizeTransformer

class ResizeTransformerTests(unittest.TestCase):
    def setUp(self):
        # Create a test image
        self.test_image = np.zeros((100, 100, 3), dtype=np.uint8)

    def test_resize_transformer_apply(self):
        # Create an instance of ResizeTransformer
        transformer = ResizeTransformer(50, 50)

        # Apply the transformation
        transformed_image = transformer.apply(self.test_image)

        # Assert the transformed image has the correct shape
        self.assertEqual(transformed_image.shape, (50, 50, 3))

    def test_resize_transformer_apply_with_none_image(self):
        # Create an instance of ResizeTransformer
        transformer = ResizeTransformer(50, 50)

        # Apply the transformation with None image
        with self.assertRaises(ImageTransformationError) as context:
            transformer.apply(None)

        # Assert the correct error message is raised
        self.assertEqual(str(context.exception), "Error transforming Image: Function parameter image: cannot be None")


if __name__ == '__main__':
    unittest.main()

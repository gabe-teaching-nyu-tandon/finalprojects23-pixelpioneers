import unittest
import numpy as np
from pixelpioneers.actions.transformers import CropTransformer
from pixelpioneers.exceptions import ImageTransformationError

class CropTransformerTestCase(unittest.TestCase):

    def test_apply(self):
        # Create a sample image
        image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        # Create a CropTransformer instance
        crop_transformer = CropTransformer(0, 0, 2, 2)

        # Apply the transformation
        transformed_image = crop_transformer.apply(image)

        # Assert the expected result
        expected_result = np.array([[1, 2], [4, 5]])
        np.testing.assert_array_equal(transformed_image, expected_result)

    def test_apply_with_invalid_image(self):
        # Create an invalid image (None)
        image = None

        # Create a CropTransformer instance
        crop_transformer = CropTransformer(0, 0, 2, 2)

        # Assert that an ImageTransformationError is raised
        with self.assertRaises(ImageTransformationError):
            crop_transformer.apply(image)


if __name__ == '__main__':
    unittest.main()

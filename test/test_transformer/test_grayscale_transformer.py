import unittest
import numpy as np
from pixelpioneers.exceptions import ImageTransformationError
from pixelpioneers.actions.transformers import GrayscaleTransformer

class GrayscaleTransformerTestCase(unittest.TestCase):
    def setUp(self):
        self.transformer = GrayscaleTransformer()

    # def test_apply_with_valid_input(self):
    #     # Arrange
    #     image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    #                       [[127, 127, 127], [255, 255, 255], [0, 0, 0]]], dtype=np.uint8)
    #
    #     expected_output = np.array([[76, 150, 29],
    #                                 [127, 255, 0]], dtype=np.uint8)
    #
    #     # Act
    #     result = self.transformer.apply(image)
    #
    #     # Assert
    #     self.assertTrue(np.array_equal(result, expected_output))

    def test_apply_with_none_image(self):
        # Arrange
        image = None

        # Act and Assert
        with self.assertRaises(ImageTransformationError):
            self.transformer.apply(image)

if __name__ == '__main__':
    unittest.main()

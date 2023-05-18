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
    #
    # def test_apply_with_none_image(self):
    #     # Arrange
    #     image = None
    #
    #     # Act and Assert
    #     with self.assertRaises(ImageTransformationError):
    #         self.transformer.apply(image)
    #
    # def test_apply_with_invalid_dimensions(self):
    #     # Arrange
    #     image = np.array([[[255, 0, 0], [0, 255, 0]],
    #                       [[127, 127, 127], [255, 255, 255]]], dtype=np.uint8)
    #
    #     # Act and Assert
    #     with self.assertRaises(ImageTransformationError):
    #         self.transformer.apply(image)
    #
    # def test_apply_with_index_error(self):
    #     # Arrange
    #     image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    #                       [[127, 127, 127], [255, 255, 255], [0, 0, 0]]], dtype=np.uint8)
    #
    #     # Change the shape to trigger IndexError
    #     image = np.reshape(image, (2, 3, 4))
    #
    #     # Act and Assert
    #     with self.assertRaises(ImageTransformationError):
    #         self.transformer.apply(image)
    #
    def test_apply_with_unknown_error(self):
        # Arrange
        image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                          [[127, 127, 127], [255, 255, 255], [0, 0, 0]]], dtype=np.uint8)

        # Force an unknown error by passing invalid arguments
        invalid_args = {'invalid_arg': 123}

        # Act and Assert
        with self.assertRaises(ImageTransformationError):
            self.transformer.apply(image, **invalid_args)

if __name__ == '__main__':
    unittest.main()

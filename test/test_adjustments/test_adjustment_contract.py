import unittest

import numpy as np

from pixelpioneers.actions.adjustments import *
from pixelpioneers.exceptions import ImageAdjustmentError


class ContrastAdjustmentTests(unittest.TestCase):
    def test_apply_with_valid_input(self):
        # Arrange
        adjustment = ContrastAdjustment(factor=2.0)
        image = np.ones((100, 100, 3), dtype=np.uint8)  # Example input image

        # Act
        result = adjustment.apply(image)

        # Assert
        self.assertIsNotNone(result)
        self.assertEqual(result.shape, image.shape)
        self.assertEqual(result.dtype, np.uint8)

    def test_apply_with_none_image(self):
        # Arrange
        adjustment = ContrastAdjustment(factor=2.0)
        image = None

        # Act & Assert
        with self.assertRaises(ImageAdjustmentError):
            adjustment.apply(image)

    def test_apply_with_invalid_dimensions(self):
        # Arrange
        adjustment = ContrastAdjustment(factor=2.0)
        image = np.ones((100, 100, 4), dtype=np.uint8)  # 4-dimensional image

        # Act & Assert
        with self.assertRaises(ImageAdjustmentError):
            adjustment.apply(image)

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()

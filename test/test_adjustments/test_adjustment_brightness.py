import numpy as np
import unittest
from pixelpioneers.actions.adjustments import *
from pixelpioneers.exceptions import ImageAdjustmentError

class BrightnessAdjustmentTest(unittest.TestCase):

    def test_apply_with_valid_input(self):
        # Arrange
        adjustment = BrightnessAdjustment(50)
        image = np.zeros((100, 100), dtype=np.uint8)  # Create a black image

        # Act
        result = adjustment.apply(image)

        # Assert
        self.assertTrue(np.array_equal(result, np.full((100, 100), 50, dtype=np.uint8)))

    def test_apply_with_invalid_brightness_value(self):
        # Arrange & Act & Assert
        with self.assertRaises(AssertionError):
            BrightnessAdjustment(300)  # Value is outside the valid range

        with self.assertRaises(AssertionError):
            BrightnessAdjustment(-300)  # Value is outside the valid range


if __name__ == '__main__':
    unittest.main()

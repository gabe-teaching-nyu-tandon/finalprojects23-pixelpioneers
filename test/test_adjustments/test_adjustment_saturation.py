import unittest

import numpy as np

from pixelpioneers.actions.adjustments import SaturationAdjustment
from pixelpioneers.exceptions import ImageTransformationError, ImageAdjustmentError


class SaturationAdjustmentTest(unittest.TestCase):

    def test_apply(self):
        adjustment = SaturationAdjustment(factor=1.5)

        # # Test case 1: Empty image
        empty_image = np.empty((0, 0, 3), dtype=np.uint8)
        with self.assertRaises(ImageAdjustmentError):
            adjustment.apply(empty_image)

        # Test case 2: Image with invalid dimensions
        invalid_image = np.array([[[100, 50, 200], [150, 75, 100]]], dtype=np.uint8)
        with self.assertRaises(ImageAdjustmentError):
            adjustment.apply(invalid_image)

        # Test case 3: Image with invalid factor
        invalid_factor = "invalid_factor"
        with self.assertRaises(ValueError):
            SaturationAdjustment(factor=invalid_factor)


if __name__ == '__main__':
    unittest.main()

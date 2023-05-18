import numpy as np

from pixelpioneers.actions.adjustments._abstract_image_adjustment import AbstractImageAdjustment
from pixelpioneers.exceptions import ImageAdjustmentError


class BrightnessAdjustment(AbstractImageAdjustment):
    name = "BrightnessAdjustment"

    def __init__(self, value: int):
        assert 255 >= value >= -255, "Invalid Brightness value - Expected value in range(-255, 256)"
        self.value = value
        super(BrightnessAdjustment, self).__init__()

    def apply(self, image: np.ndarray) -> np.ndarray:
        try:
            assert image is not None, "Function parameter image: cannot be None"

            # Convert image to float to avoid overflow
            img_float = image.astype(np.float32)

            # Apply brightness adjustment
            img_float += self.value

            # Clip the values to [0, 255] and convert back to uint8
            img_adjusted = np.clip(img_float, 0, 255).astype(np.uint8)
            return img_adjusted
        
        except AssertionError as ae:
            raise ImageAdjustmentError(f"Error adjusting Image: {ae}")

        except Exception as e:
            raise ImageAdjustmentError(f"Error adjusting Image: Unknown Error")


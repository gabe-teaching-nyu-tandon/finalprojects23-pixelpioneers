import numpy as np

from pixelpioneers.actions.adjustments._abstract_image_adjustment import AbstractImageAdjustment
from pixelpioneers.exceptions import ImageTransformationError


class BrightnessAdjustment(AbstractImageAdjustment):
    name = "BrightnessAdjustment"

    def __init__(self, value: int):
        self.value = value
        super(BrightnessAdjustment, self).__init__()

    def apply(self, image: np.ndarray) -> np.ndarray:
        # Convert image to float to avoid overflow
        img_float = image.astype(np.float32)

        # Apply brightness adjustment
        img_float += self.value

        # Clip the values to [0, 255] and convert back to uint8
        img_adjusted = np.clip(img_float, 0, 255).astype(np.uint8)
        return img_adjusted

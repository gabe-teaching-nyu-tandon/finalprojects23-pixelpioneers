import colorsys

import numpy as np

from pixelpioneers.actions.adjustments._abstract_image_adjustment import AbstractImageAdjustment
from pixelpioneers.exceptions import ImageAdjustmentError

class SaturationAdjustment(AbstractImageAdjustment):
    name = "SaturationAdjustment"

    def __init__(self, factor: float | int):
        if not (isinstance(self.factor, int) or isinstance(self.factor, float)):
            raise ValueError("Invalid factor. Expected a numeric value.")
        self.factor = factor

    def apply(self, image: np.ndarray) -> np.ndarray:
        try:
     
            # Convert the image to float32 for processing
            float_image = image.astype(np.float32) / 255

            # Convert RGB to HSV
            hsv_image = np.apply_along_axis(colorsys.rgb_to_hsv, 2, float_image)

            # Adjust the saturation
            hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * self.factor, 0, 1)

            # Convert HSV back to RGB
            adjusted_image = np.apply_along_axis(colorsys.hsv_to_rgb, 2, hsv_image)

            # Convert back to uint8 and return
            return (adjusted_image * 255).astype(np.uint8)
        except AssertionError as ae:
            raise ImageAdjustmentError(f"Error adjusting Image: {ae}")

        except Exception as e:
            raise ImageAdjustmentError(f"Error adjusting Image: Unknown Error")


import numpy as np

from pixelpioneers.actions.adjustments._abstract_image_adjustment import AbstractImageAdjustment
from pixelpioneers.exceptions import ImageAdjustmentError


class ContrastAdjustment(AbstractImageAdjustment):
    name = "ContrastAdjustment"

    def __init__(self, factor: float | int):
        self.factor = factor
        super(ContrastAdjustment, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:
            assert image is not None, "Function parameter image: cannot be None"
            assert image.ndim == 3, f"Expected a 3 dimensional image, Instead got a image with {image.ndim} dimensions"
            
            # Calculate the mean color value for each channel
            mean = np.mean(image, axis=(0, 1), keepdims=True)

            # Adjust the contrast
            adjusted_image = mean + (image - mean) * self.factor
            adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)

            return adjusted_image
        
        except AssertionError as ae:
            raise ImageAdjustmentError(f"Error adjusting Image: {ae}")

        except Exception as e:
            raise ImageAdjustmentError(f"Error adjusting Image: Unknown Error")


    
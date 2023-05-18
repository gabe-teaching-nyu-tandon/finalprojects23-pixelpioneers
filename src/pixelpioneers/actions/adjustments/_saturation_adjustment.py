import colorsys

import numpy as np
import logging
from pixelpioneers.actions.adjustments._abstract_image_adjustment import AbstractImageAdjustment
from pixelpioneers.exceptions import ImageAdjustmentError

logger = logging.getLogger(__name__)

class SaturationAdjustment(AbstractImageAdjustment):
    name = "SaturationAdjustment"

    def __init__(self, factor: float):
        if not (isinstance(factor, int) or isinstance(factor, float)):
            raise ValueError("Invalid factor. Expected a numeric value.")
        self.factor = factor

    def apply(self, image: np.ndarray) -> np.ndarray:
        try:

            assert image is not None, "Function parameter image: cannot be None"
            assert image.ndim == 3, f"Expected a 3 dimensional image, Insted got a image with {image.ndim} dimensions"

            # Convert the image to float32 for processing
            logger.info("Converting image to float32 for processing")
            float_image = image.astype(np.float32) / 255

            # Convert RGB to HSV
            logger.info("Converting RGB to HSV")
            hsv_image = np.apply_along_axis(colorsys.rgb_to_hsv, 2, float_image)

            # Adjust the saturation
            logger.info("Adjusting the saturation")
            hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * self.factor, 0, 1)

            # Convert HSV back to RGB
            logger.info("Converting HSV back to RGB")
            adjusted_image = np.apply_along_axis(colorsys.hsv_to_rgb, 2, hsv_image)

            # Convert back to uint8 and return
            logger.info("Converting back to uint8 and returning")
            return (adjusted_image * 255).astype(np.uint8)

        except AssertionError as ae:
            logger.error(f"Error transforming image: {ae}")
            raise ImageAdjustmentError(f"Error transforming Image: {ae}")

        except Exception as e:
            logger.exception("Error transforming image: Unknown Error")
            raise ImageAdjustmentError(f"Error transforming Image: Unknown Error")

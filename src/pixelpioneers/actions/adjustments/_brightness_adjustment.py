import numpy as np
import logging

from pixelpioneers.actions.adjustments._abstract_image_adjustment import AbstractImageAdjustment
from pixelpioneers.exceptions import ImageAdjustmentError

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BrightnessAdjustment(AbstractImageAdjustment):
    """
    Adjusts the brightness of an image.

    This class inherits from the AbstractImageAdjustment class and provides a method
    to adjust the brightness of an image.

    :param value: The amount of brightness adjustment. Should be an integer in the range
                  [-255, 255].
    :type value: int
    """
    name = "BrightnessAdjustment"

    def __init__(self, value: int):
        """
        Initializes a BrightnessAdjustment object.

        It validates the input value and sets it as the brightness adjustment value.

        :param value: The amount of brightness adjustment.
        :type value: int
        :raises AssertionError: If the value is not in the range [-255, 255].
        """
        assert 255 >= value >= -255, "Invalid Brightness value - Expected value in range(-255, 256)"
        self.value = value
        super(BrightnessAdjustment, self).__init__()

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Applies the brightness adjustment to the given image.

        :param image: The input image to apply the brightness adjustment to.
        :type image: np.ndarray
        :return: The adjusted image with the brightness adjustment applied.
        :rtype: np.ndarray
        :raises ImageTransformationError: If the input image is None or if any error occurs during
                                          the transformation process.
        """
        try:
            assert image is not None, "Function parameter image: cannot be None"
            logger.info("Applying brightness adjustment to the image.")

            # Convert image to float to avoid overflow
            img_float = image.astype(np.float32)

            # Apply brightness adjustment
            img_float += self.value
            logger.info(f"Brightness adjustment value: {self.value}")

            # Clip the values to [0, 255] and convert back to uint8
            img_adjusted = np.clip(img_float, 0, 255).astype(np.uint8)
            logger.info("Brightness adjustment applied successfully.")

            return img_adjusted
        
        except AssertionError as ae:
            logger.error(f"Error transforming Image: {ae}")
            raise ImageAdjustmentError(f"Error adjusting Image: {ae}")

        except Exception as e:
            logger.error("Error transforming Image: Unknown Error")
            raise ImageAdjustmentError(f"Error adjusting Image: {ae}")

        except Exception as e:
            raise ImageAdjustmentError(f"Error adjusting Image: Unknown Error")


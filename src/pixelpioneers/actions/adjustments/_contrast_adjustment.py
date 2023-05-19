import numpy as np

from pixelpioneers.actions.adjustments._abstract_image_adjustment import AbstractImageAdjustment
from pixelpioneers.exceptions import ImageAdjustmentError


class ContrastAdjustment(AbstractImageAdjustment):
    """
    Adjusts the contrast of an image based on a given factor.

    This class inherits from `AbstractImageAdjustment` and provides the functionality to adjust the contrast of an image.

    Args:
        factor (float): The factor by which to adjust the contrast of the image.

    Attributes:
        factor (float): The factor by which the contrast is adjusted.

    Raises:
        ImageAdjustmentError: If the image is None, has an incorrect number of dimensions, or an unknown error occurs during transformation.
    """
    name = "ContrastAdjustment"

    def __init__(self, factor: float):
        """
        Initializes a new instance of the ContrastAdjustment class.

        Args:
            factor (float): The factor by which to adjust the contrast of the image.
        """
        self.factor = factor
        super(ContrastAdjustment, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Applies the contrast adjustment to the given image.

        Args:
            image (np.ndarray): The image to which the contrast adjustment should be applied.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            np.ndarray: The adjusted image.

        Raises:
            ImageAdjustmentError: If the image is None, has an incorrect number of dimensions, or an unknown error occurs during transformation.
        """
        try:

            assert image is not None, "Function parameter image: cannot be None"
            assert image.ndim == 3, f"Expected a 3 dimensional image, Instead got a image with {image.ndim} dimensions"
            assert image.shape[-1] == 3, f"Expected a 3, Instead got a image with {image.shape[-1]} dimensions "
            # Calculate the mean color value for each channel
            mean = np.mean(image, axis=(0, 1), keepdims=True)

            # Adjust the contrast
            adjusted_image = mean + (image - mean) * self.factor
            adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)

            return adjusted_image

        except AssertionError as ae:
            raise ImageAdjustmentError(f"Error transforming Image: {ae}")

        except Exception as e:
            raise ImageAdjustmentError(f"Error transforming Image: Unknown Error")

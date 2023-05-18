import logging

import cv2
import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError

logging.basicConfig(level=logging.INFO)  # Set the desired logging level


class ResizeTransformer(AbstractImageTransformer):
    """
    ResizeTransformer is an image transformer that resizes an image to a specified width and height.

    Args:
        width (int): The desired width of the resized image.
        height (int): The desired height of the resized image.
    """

    def __init__(self, width: int, height: int):
        self.size = [width, height]
        super(ResizeTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Applies the resizing transformation to the given image.

        Args:
            image (numpy.ndarray): The input image to be resized.

        Returns:
            numpy.ndarray: The resized image.

        Raises:
            ImageTransformationError: If the image is None or if an error occurs during the transformation.
        """
        try:

            assert image is not None, "Function parameter image: cannot be None"
            logging.info("Resizing image")
            logging.info("Image resized successfully")
            return cv2.resize(image, self.size, interpolation=cv2.INTER_AREA)

        except AssertionError as ae:
            logging.error(f"Error transforming Image: {ae}")
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except Exception as e:
            logging.error("Error transforming Image: Unknown Error")
            raise ImageTransformationError("Error transforming Image: Unknown Error")

import logging

import cv2
import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class RotateTransformer(AbstractImageTransformer):
    """
    A class representing an image rotation transformer.

    This transformer rotates an input image by a specified angle using OpenCV.

    :param angle: The angle (in degrees) by which to rotate the image.
    """

    def __init__(self, angle):
        """
        Initialize the RotateTransformer instance.

        :param angle: The angle (in degrees) by which to rotate the image.
        """
        self.angle = angle
        super(RotateTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Apply the rotation transformation to the input image.

        :param image: The input image to be rotated.
        :param args: Additional positional arguments (unused).
        :param kwargs: Additional keyword arguments (unused).
        :return: The rotated image.
        :raises ImageTransformationError: If an error occurs during the image transformation.
        """
        try:

            assert image is not None, "Function parameter image: cannot be None"
            logger.info("Starting image rotation")

            height, width = image.shape[:2]
            center = (width // 2, height // 2)
            rotation_matrix = cv2.getRotationMatrix2D(center, self.angle, 1.0)
            logger.info("Image rotation successful")

            return cv2.warpAffine(image, rotation_matrix, (width, height))

        except AssertionError as ae:
            logger.error(f"Error transforming Image: {ae}")
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except Exception as e:
            logger.error("Error transforming Image: Unknown Error")
            raise ImageTransformationError("Error transforming Image: Unknown Error")

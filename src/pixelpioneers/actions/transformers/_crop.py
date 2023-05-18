import logging

import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError

logger = logging.getLogger(__name__)


class CropTransformer(AbstractImageTransformer):
    """
    A transformer class for cropping an image.

    :param x1: The starting x-coordinate of the crop box.
    :type x1: int
    :param y1: The starting y-coordinate of the crop box.
    :type y1: int
    :param x2: The ending x-coordinate of the crop box.
    :type x2: int
    :param y2: The ending y-coordinate of the crop box.
    :type y2: int
    """

    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        """
        Initialize the CropTransformer instance.

        :param x1: The starting x-coordinate of the crop box.
        :type x1: int
        :param y1: The starting y-coordinate of the crop box.
        :type y1: int
        :param x2: The ending x-coordinate of the crop box.
        :type x2: int
        :param y2: The ending y-coordinate of the crop box.
        :type y2: int
        """
        self.box = (x1, y1, x2, y2)
        super(CropTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Apply the crop transformation to the given image.

        :param image: The input image as a NumPy array.
        :type image: np.ndarray
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The cropped image as a NumPy array.
        :rtype: np.ndarray
        :raises ImageTransformationError: If there is an error during the transformation.
        """
        try:

            assert image is not None, "Function parameter image: cannot be None"
            logger.info("Applying crop transformation")
            x1, y1, x2, y2 = self.box
            return image[y1:y2, x1:x2]

        except AssertionError as ae:
            logger.error(f"Error transforming Image: {ae}")
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except IndexError:
            logger.error("Error transforming Image: the bounds are out of range")
            raise ImageTransformationError("Error transforming Image: the bounds are out of range")

        except Exception as e:
            logger.error("Error transforming Image: Unknown Error")
            raise ImageTransformationError("Error transforming Image: Unknown Error")

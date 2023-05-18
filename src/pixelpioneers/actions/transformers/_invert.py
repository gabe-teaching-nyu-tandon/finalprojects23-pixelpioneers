import logging

import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError


class InvertTransformer(AbstractImageTransformer):
    """
    A transformer that inverts the colors of an image.

    This transformer applies an inversion operation on the input image, resulting in the colors being inverted.
    For example, white becomes black and vice versa.

    Inherits from :class:`AbstractImageTransformer`.

    :param AbstractImageTransformer: The base class for image transformers.
    """

    def __init__(self):
        """
        Initialize the InvertTransformer object.
        """
        super(InvertTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Apply the inversion operation on the input image.

        This method takes an input image as a NumPy array and applies the inversion operation by subtracting each pixel
        value from 255. The resulting image will have inverted colors.

        :param image: The input image as a NumPy array.
        :type image: np.ndarray
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The inverted image as a NumPy array.
        :rtype: np.ndarray
        :raises ImageTransformationError: If an error occurs during the image transformation.
        """
        try:

            assert image is not None, "Function parameter image: cannot be None"
            assert image.ndim == 3, f"Expected a 3 dimensional image, Instead got a image with {image.ndim} dimensions"
            logging.info("Image transformation started")
            return 255 - image

        except AssertionError as ae:
            logging.error(f"AssertionError occurred: {ae}")
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except IndexError:
            logging.error("IndexError occurred: the bounds are out of range")
            raise ImageTransformationError("Error transforming Image: the bounds are out of range")

        except Exception as e:
            logging.error(f"Exception occurred: {e}")
            raise ImageTransformationError("Error transforming Image: Unknown Error")

import numpy as np
import logging
from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError


class GrayscaleTransformer(AbstractImageTransformer):
    """
    GrayscaleTransformer is a class that applies grayscale transformation to an image.

    This class inherits from the AbstractImageTransformer class.

    Attributes:
        None

    Methods:
        apply(image: np.ndarray, *args, **kwargs) -> np.ndarray:
            Applies grayscale transformation to the input image.

    """

    def __init__(self):
        """
        Initialize the GrayscaleTransformer instance.

        Args:
            None

        Returns:
            None
        """
        super(GrayscaleTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Applies grayscale transformation to the input image.

        Args:
            image (np.ndarray): The input image as a NumPy array.

        Returns:
            np.ndarray: The grayscale transformed image as a NumPy array.

        Raises:
            ImageTransformationError: If the input image is None or has incorrect dimensions.
            ImageTransformationError: If the bounds of the image are out of range.
            ImageTransformationError: If an unknown error occurs during the transformation.
        """
        try:
            assert image is not None, "Function parameter image: cannot be None"
            logging.info("Image parameter is not None")

            assert image.ndim == 3, f"Expected a 3 dimensional image, Instead got a image with {image.ndim} dimensions"
            logging.info(f"Image dimensions: {image.ndim}")

            logging.info("Grayscale transformation applied successfully")
            return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

        except AssertionError as ae:
            logging.error(f"Error transforming Image: {ae}")
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except IndexError:
            logging.error("Error transforming Image: the bounds are out of range")
            raise ImageTransformationError("Error transforming Image: the bounds are out of range")

        except Exception as e:
            logging.error("Error transforming Image: Unknown Error")
            raise ImageTransformationError("Error transforming Image: Unknown Error")

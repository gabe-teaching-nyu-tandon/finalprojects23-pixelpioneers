import cv2
import numpy as np
import logging
from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FlipTransformer(AbstractImageTransformer):
    """
    Transformer that flips an image horizontally or vertically.

    Args:
        mode (str): The mode of the flip transformation. Supported values are "horizontal" and "vertical".

    Raises:
        ImageTransformationError: If there is an error during the image transformation.

    """
    def __init__(self, mode: str):
        self.mode = mode
        super(FlipTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Applies the flip transformation to the given image.

        Args:
            image (np.ndarray): The input image to be transformed.
            *args: Additional positional arguments (unused).
            **kwargs: Additional keyword arguments (unused).

        Returns:
            np.ndarray: The transformed image.

        Raises:
            ImageTransformationError: If there is an error during the image transformation.

        """
        try:
            assert image is not None, "Function parameter image: cannot be None"
            logger.info("Image received for transformation")
            if self.mode.lower() == "horizontal":
                logger.info("Applying horizontal flip transformation")
                return cv2.flip(image, 1)
            elif self.mode.lower() == "vertical":
                logger.info("Applying vertical flip transformation")
                return cv2.flip(image, 0)

        except AssertionError as ae:
            logger.error(f"AssertionError: {ae}")
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except Exception as e:
            logger.error(f"Unknown Error: {e}")
            raise ImageTransformationError(f"Error transforming Image: Unknown Error")

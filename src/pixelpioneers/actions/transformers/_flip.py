import cv2
import numpy as np
from enum import Enum

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError


class FlipMode(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class FlipTransformer(AbstractImageTransformer):
    """
    A transformer that flips an image horizontally or vertically.
    """

    def __init__(self, mode: FlipMode):
        """
        Initializes a new instance of the FlipTransformer class.

        :param mode: The flip mode (horizontal or vertical).
        """
        self.mode = mode

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        """
        Applies the flip transformation to the image.

        :param image: The input image.
        :return: The flipped image.
        """
        if image is None:
            raise ImageTransformationError("Function parameter image: cannot be None")

        if self.mode == FlipMode.HORIZONTAL:
            return cv2.flip(image, 1)
        elif self.mode == FlipMode.VERTICAL:
            return cv2.flip(image, 0)

        raise ImageTransformationError(f"Invalid flip mode: {self.mode}")
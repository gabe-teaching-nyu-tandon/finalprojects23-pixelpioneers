import cv2
import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError


class FlipTransformer(AbstractImageTransformer):

    def __init__(self, mode: str):
        self.mode = mode
        super(FlipTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:

            assert image is not None, "Function parameter image: cannot be None"

            if self.mode.lower() == "horizontal":
                return cv2.flip(image, 1)
            elif self.mode.lower() == "vertical":
                return cv2.flip(image, 0)

        except AssertionError as ae:
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except Exception as e:
            raise ImageTransformationError(f"Error transforming Image: Unknown Error")

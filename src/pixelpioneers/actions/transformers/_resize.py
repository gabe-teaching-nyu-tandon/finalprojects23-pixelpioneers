import cv2
import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError


class ResizeTransformer(AbstractImageTransformer):

    def __init__(self, width: int, height: int):
        self.size = [width, height]
        super(ResizeTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:

            assert image is not None, "Function parameter image: cannot be None"

            return cv2.resize(image, self.size, interpolation=cv2.INTER_AREA)

        except AssertionError as ae:
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except Exception as e:
            raise ImageTransformationError("Error transforming Image: Unknown Error")

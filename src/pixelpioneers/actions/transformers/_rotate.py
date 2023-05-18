import cv2
import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError


class RotateTransformer(AbstractImageTransformer):

    def __init__(self, angle):
        self.angle = angle
        super(RotateTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:

            assert image is not None, "Function parameter image: cannot be None"

            height, width = image.shape[:2]
            center = (width // 2, height // 2)
            rotation_matrix = cv2.getRotationMatrix2D(center, self.angle, 1.0)
            return cv2.warpAffine(image, rotation_matrix, (width, height))

        except AssertionError as ae:
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except Exception as e:
            raise ImageTransformationError("Error transforming Image: Unknown Error")

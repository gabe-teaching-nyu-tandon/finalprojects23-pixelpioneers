import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError


class CropTransformer(AbstractImageTransformer):

    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.box = (x1, y1, x2, y2)
        super(CropTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:

            assert image is not None, "Function parameter image: cannot be None"

            x1, y1, x2, y2 = self.box
            return image[y1:y2, x1:x2]

        except AssertionError as ae:
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except IndexError:
            raise ImageTransformationError("Error transforming Image: the bounds are out of range")

        except Exception as e:
            raise ImageTransformationError("Error transforming Image: Unknown Error")

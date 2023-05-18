import numpy as np

from pixelpioneers.actions.transformers._abstract_image_transformer import AbstractImageTransformer
from pixelpioneers.exceptions import ImageTransformationError


class InvertTransformer(AbstractImageTransformer):

    def __init__(self):
        super(InvertTransformer, self).__init__()

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:

            assert image is not None, "Function parameter image: cannot be None"
            assert image.ndim == 3, f"Expected a 3 dimensional image, Instead got a image with {image.ndim} dimensions"

            return 255 - image

        except AssertionError as ae:
            raise ImageTransformationError(f"Error transforming Image: {ae}")

        except IndexError:
            raise ImageTransformationError("Error transforming Image: the bounds are out of range")

        except Exception as e:
            raise ImageTransformationError("Error transforming Image: Unknown Error")

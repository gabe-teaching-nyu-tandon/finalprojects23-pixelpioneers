import numpy as np
from abc import ABC, abstractmethod

class InvalidImageArray(Exception):
    pass

class AbstractImageTransformer(ABC):
    @abstractmethod
    def transform_image(self, image: np.ndarray) -> np.ndarray:
        pass

class GrayscaleTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray) -> np.ndarray:
        if image is None or image.ndim != 3 or image.shape[-1] != 3:
            raise InvalidImageArray("Invalid or corrupted image array. Must be a 3D array with 3 channels.")

        grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
        return np.stack((grayscale_image,) * 3, axis=-1)

class ImageTransformerFactory:
    transformers = {
        "grayscale": GrayscaleTransformer
    }

    @staticmethod
    def get_transformer(transform: str) -> AbstractImageTransformer:
        if transform.lower() in ImageTransformerFactory.transformers:
            return ImageTransformerFactory.transformers[transform.lower()]()
        else:
            raise KeyError(f"Unsupported transformation: {transform}")

class UnifiedImageTransformer(AbstractImageTransformer):
    def transform_image(self, transform: str, image: np.ndarray) -> np.ndarray:
        try:
            transformer = ImageTransformerFactory.get_transformer(transform)
            return transformer.transform_image(image)
        except KeyError as e:
            print(e)
            return None
        except InvalidImageArray as e:
            print(e)
            return None
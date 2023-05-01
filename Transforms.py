import numpy as np
from abc import ABC, abstractmethod

class UnsupportedTransformException(Exception):
    pass

class AbstractImageTransformer(ABC):
    @abstractmethod
    def transform_image(self, image: np.ndarray) -> np.ndarray:
        pass

class GrayscaleTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray) -> np.ndarray:
        if image.ndim == 3:
            return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
        elif image.ndim == 2:
            return image
        else:
            raise ValueError("Invalid image dimensions. Expected 2 or 3 dimensions.")

class ImageTransformerFactory:
    transformers = {
        "grayscale": GrayscaleTransformer,
    }

    @staticmethod
    def get_transformer(transform: str) -> AbstractImageTransformer:
        if transform.lower() in ImageTransformerFactory.transformers:
            return ImageTransformerFactory.transformers[transform.lower()]()
        else:
            raise UnsupportedTransformException(f"Unsupported transform: {transform}")

class UnifiedImageTransformer(AbstractImageTransformer):
    def transform_image(self, transform: str, image: np.ndarray) -> np.ndarray:
        try:
            transformer = ImageTransformerFactory.get_transformer(transform)
            return transformer.transform_image(image)
        except UnsupportedTransformException as e:
            print(e)
            return None
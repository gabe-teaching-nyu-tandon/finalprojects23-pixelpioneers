import numpy as np
from abc import ABC, abstractmethod
from PIL import Image

class UnsupportedTransformException(Exception):
    pass

class AbstractImageTransformer(ABC):
    @abstractmethod
    def transform_image(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        pass

class GrayscaleTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        if image.ndim == 3:
            return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
        elif image.ndim == 2:
            return image
        else:
            raise ValueError("Invalid image dimensions. Expected 2 or 3 dimensions.")

class ResizeTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, size: tuple, *args, **kwargs) -> np.ndarray:
        img = Image.fromarray(image)
        img_resized = img.resize(size)
        return np.array(img_resized)

class RotateTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, angle: float, *args, **kwargs) -> np.ndarray:
        img = Image.fromarray(image)
        img_rotated = img.rotate(angle)
        return np.array(img_rotated)

class FlipTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, mode: str, *args, **kwargs) -> np.ndarray:
        img = Image.fromarray(image)
        if mode.lower() == "horizontal":
            img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode.lower() == "vertical":
            img_flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("Invalid flip mode. Expected 'horizontal' or 'vertical'.")
        return np.array(img_flipped)

class CropTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, box: tuple, *args, **kwargs) -> np.ndarray:
        img = Image.fromarray(image)
        img_cropped = img.crop(box)
        return np.array(img_cropped)

class ImageTransformerFactory:
    transformers = {
        "grayscale": GrayscaleTransformer,
        "resize": ResizeTransformer,
        "rotate": RotateTransformer,
        "flip": FlipTransformer,
        "crop": CropTransformer,
    }

    @staticmethod
    def get_transformer(transform: str) -> AbstractImageTransformer:
        if transform.lower() in ImageTransformerFactory.transformers:
            return ImageTransformerFactory.transformers[transform.lower()]()
        else:
            raise UnsupportedTransformException(f"Unsupported transform: {transform}")

class UnifiedImageTransformer(AbstractImageTransformer):
    def transform_image(self, transform: str, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:
            transformer = ImageTransformerFactory.get_transformer(transform)
            return transformer.transform_image(image, *args, **kwargs)
        except UnsupportedTransformException as e:
            print(e)
            return None
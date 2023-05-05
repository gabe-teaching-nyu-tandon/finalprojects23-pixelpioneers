import numpy as np
from abc import ABC, abstractmethod

class UnsupportedTransformException(Exception):
    pass

class AbstractImageTransformer(ABC):
    @abstractmethod
    def transform_image(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        pass

class GrayscaleTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        if image is None:
            print("Error: Image is None, cannot convert to grayscale.")
            return None
        try:
            if image.ndim == 3:
                return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
            elif image.ndim == 2:
                return image
            else:
                raise ValueError("Invalid image dimensions. Expected 2 or 3 dimensions.")
        except Exception as e:
            print(f"Error converting image to grayscale: {e}")
            return None

class ResizeTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, size=None, *args, **kwargs) -> np.ndarray:
        if image is None:
            print("Error: Image is None, cannot resize.")
            return None
        if size is None:
            print("Error: Size not provided for resizing.")
            return image
        try:
            return cv2.resize(image, size)
        except Exception as e:
            print(f"Error resizing image: {e}")
            return None

class RotateTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, angle=None, *args, **kwargs) -> np.ndarray:
        if image is None:
            print("Error: Image is None, cannot rotate.")
            return None
        if angle is None:
            print("Error: Angle not provided for rotation.")
            return image
        try:
            height, width = image.shape[:2]
            center = (width // 2, height // 2)
            rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
            return cv2.warpAffine(image, rotation_matrix, (width, height))
        except Exception as e:
            print(f"Error rotating image: {e}")
            return None

class FlipTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, mode="horizontal", *args, **kwargs) -> np.ndarray:
        if image is None:
            print("Error: Image is None, cannot flip.")
            return None
        try:
            if mode.lower() == "horizontal":
                return cv2.flip(image, 1)
            elif mode.lower() == "vertical":
                return cv2.flip(image, 0)
            else:
                raise ValueError("Invalid flip mode. Expected 'horizontal' or 'vertical'.")
        except Exception as e:
            print(f"Error flipping image: {e}")
            return None

class CropTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, box=None, *args, **kwargs) -> np.ndarray:
        if image is None:
            print("Error: Image is None, cannot crop.")
            return None
        if box is None:
            print("Error: Box not provided for cropping.")
            return image
        try:
            x1, y1, x2, y2 = box
            return image[y1:y2, x1:x2]
        except Exception as e:
            print(f"Error cropping image: {e}")
            return None
        
class InvertColorTransformer(AbstractImageTransformer):
    def transform_image(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:
            if image is None:
                raise ValueError("Input image is None.")
            if image.ndim != 3 and image.ndim != 2:
                raise ValueError("Invalid image dimensions. Expected 2 or 3 dimensions.")
            return 255 - image
        except Exception as e:
            print(f"Error inverting colors: {e}")
            return None

class ImageTransformerFactory:
    transformers = {
        "grayscale": GrayscaleTransformer,
        "resize": ResizeTransformer,
        "rotate": RotateTransformer,
        "flip": FlipTransformer,
        "crop": CropTransformer,
        "invert": InvertColorTransformer,
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
        except Exception as e:
            print(f"Error applying transformation: {e}")
            return None
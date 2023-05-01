from IO_Class import UnifiedImageHandler, UnsupportedFileFormatException
from Transforms import UnifiedImageTransformer, UnsupportedTransformException
import numpy as np

class ImageProcessingInterface:
    def __init__(self):
        self.image_handler = UnifiedImageHandler()
        self.image_transformer = UnifiedImageTransformer()

    def read_image(self, filepath: str) -> np.ndarray:
        try:
            return self.image_handler.read_image(filepath)
        except UnsupportedFileFormatException as e:
            print(e)
            return None
        except Exception as e:
            print(f"Error reading image: {e}")
            return None

    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        if image is None:
            print("Error: Image is None, cannot save.")
            return False
        try:
            return self.image_handler.write_image(filepath, image)
        except UnsupportedFileFormatException as e:
            print(e)
            return False
        except Exception as e:
            print(f"Error writing image: {e}")
            return False

    def apply_transform(self, transform: str, image: np.ndarray) -> np.ndarray:
        if image is None:
            print("Error: Image is None, cannot apply transformation.")
            return None
        try:
            return self.image_transformer.transform_image(transform, image)
        except UnsupportedTransformException as e:
            print(e)
            return None
        except Exception as e:
            print(f"Error applying transformation: {e}")
            return None
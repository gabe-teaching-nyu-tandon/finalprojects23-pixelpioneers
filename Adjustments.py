import numpy as np
from abc import ABC, abstractmethod

class UnsupportedAdjustmentException(Exception):
    pass

class AbstractImageAdjustment(ABC):
    @abstractmethod
    def apply_adjustment(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        pass

class BrightnessAdjustment(AbstractImageAdjustment):
    def apply_adjustment(self, image: np.ndarray, value: float) -> np.ndarray:
        if image is None:
            raise ValueError("Image is None, cannot apply brightness adjustment.")

        if image.ndim < 2 or image.ndim > 3:
            raise ValueError("Invalid image dimensions. Expected 2 or 3 dimensions.")

        if not (-255.0 <= value <= 255.0):
            raise ValueError("Invalid brightness adjustment value. Expected a value between -255 and 255.")

        try:
            # Convert image to float to avoid overflow
            img_float = image.astype(np.float32)

            # Apply brightness adjustment
            img_float += value

            # Clip the values to [0, 255] and convert back to uint8
            img_adjusted = np.clip(img_float, 0, 255).astype(np.uint8)
            return img_adjusted
        except Exception as e:
            raise ValueError(f"Error adjusting brightness: {e}")

class ImageAdjustmentFactory:
    adjustments = {
        "brightness": BrightnessAdjustment,
    }

    @staticmethod
    def get_adjustment(adjustment: str) -> AbstractImageAdjustment:
        if adjustment.lower() in ImageAdjustmentFactory.adjustments:
            return ImageAdjustmentFactory.adjustments[adjustment.lower()]()
        else:
            raise UnsupportedAdjustmentException(f"Unsupported adjustment: {adjustment}")

class UnifiedImageAdjustment(AbstractImageAdjustment):
    def apply_adjustment(self, adjustment: str, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:
            adjuster = ImageAdjustmentFactory.get_adjustment(adjustment)
            return adjuster.apply_adjustment(image, *args, **kwargs)
        except UnsupportedAdjustmentException as e:
            print(e)
            return None
        except ValueError as e:
            print(e)
            return None
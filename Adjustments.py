import numpy as np
from abc import ABC, abstractmethod

class UnsupportedAdjustmentException(Exception):
    pass

class AbstractImageAdjustment(ABC):
    @abstractmethod
    def apply_adjustment(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        pass

class BrightnessAdjustment(AbstractImageAdjustment):
    def apply_adjustment(self, image: np.ndarray, factor: float) -> np.ndarray:
        if image is None:
            raise ValueError("Invalid image input. Image is None.")

        if image.ndim != 3 or image.shape[2] != 3:
            raise ValueError("Invalid image dimensions. Expected 3 dimensions with 3 color channels.")

        if not isinstance(factor, (int, float)):
            raise ValueError("Invalid factor input. Expected int or float value.")

        adjusted_image = np.clip(image * factor, 0, 255).astype(np.uint8)
        return adjusted_image

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
import numpy as np
import colorsys
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

class ContrastAdjustment(AbstractImageAdjustment):
    def adjust_image(self, image: np.ndarray, factor: float) -> np.ndarray:
        try:
            if not (isinstance(factor, int) or isinstance(factor, float)):
                raise ValueError("Invalid factor. Expected a numeric value.")
            if image.ndim != 3 or image.shape[2] != 3:
                raise ValueError("Invalid image dimensions. Expected 3 dimensions with 3 color channels.")

            # Calculate the mean color value for each channel
            mean = np.mean(image, axis=(0, 1), keepdims=True)

            # Adjust the contrast
            adjusted_image = mean + (image - mean) * factor
            adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)

            return adjusted_image
        except ValueError as e:
            print(f"Error adjusting contrast: {e}")
            return image.copy()  # Fallback: return the original image as a copy
        except Exception as e:
            print(f"Unexpected error adjusting contrast: {e}")
            return image.copy()  # Fallback: return the original image as a copy

class SaturationAdjustment(AbstractImageAdjustment):
    def adjust_image(self, image: np.ndarray, factor: float) -> np.ndarray:
        try:
            if not (isinstance(factor, int) or isinstance(factor, float)):
                raise ValueError("Invalid factor. Expected a numeric value.")
            if image.ndim != 3 or image.shape[2] != 3:
                raise ValueError("Invalid image dimensions. Expected 3 dimensions with 3 color channels.")

            # Convert the image to float32 for processing
            float_image = image.astype(np.float32) / 255

            # Convert RGB to HSV
            hsv_image = np.apply_along_axis(colorsys.rgb_to_hsv, 2, float_image)

            # Adjust the saturation
            hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * factor, 0, 1)

            # Convert HSV back to RGB
            adjusted_image = np.apply_along_axis(colorsys.hsv_to_rgb, 2, hsv_image)

            # Convert back to uint8 and return
            return (adjusted_image * 255).astype(np.uint8)
        except ValueError as e:
            print(f"Error adjusting saturation: {e}")
            return image.copy()  # Fallback: return the original image as a copy
        except Exception as e:
            print(f"Unexpected error adjusting saturation: {e}")
            return image.copy()  # Fallback: return the original image as a copy

class ImageAdjustmentFactory:
    adjustments = {
        "brightness": BrightnessAdjustment,
        "contrast": ContrastAdjustment,
        "saturation": SaturationAdjustment,
    }

    @staticmethod
    def get_adjustment(adjustment: str) -> AbstractImageAdjustment:
        if adjustment.lower() in ImageAdjustmentFactory.adjustments:
            return ImageAdjustmentFactory.adjustments[adjustment.lower()]()
        else:
            raise UnsupportedAdjustmentException(f"Unsupported adjustment: {adjustment}")

class UnifiedImageAdjustment(AbstractImageAdjustment):
    def adjust_image(self, adjustment: str, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        try:
            adjuster = ImageAdjustmentFactory.get_adjustment(adjustment)
            return adjuster.adjust_image(image, *args, **kwargs)
        except UnsupportedAdjustmentException as e:
            print(e)
            return None
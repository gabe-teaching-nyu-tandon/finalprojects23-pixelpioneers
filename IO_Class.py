import struct
import numpy as np
from abc import ABC, abstractmethod
import os
from PIL import Image

class AbstractImageHandler(ABC):
    @abstractmethod
    def read_image(self, filepath: str) -> np.ndarray:
        pass

    @abstractmethod
    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        pass

class BMPHandler(AbstractImageHandler):
    def read_image(self, filepath: str) -> np.ndarray:
        try:
            with open(filepath, 'rb') as f:
                header = f.read(54)
                width, height, bits_per_pixel = struct.unpack("<3I", header[18:30])
                data = f.read()
        except IOError:
            print(f"Error: Unable to open file '{filepath}'.")
            return None
        except struct.error:
            print("Error: Invalid BMP header.")
            return None

        # Calculate the padding for each row
        padding = (4 - (width * 3) % 4) % 4

        try:
            image_array = np.zeros((height, width, 3), dtype=np.uint8)

            # Parse the image data into a NumPy array
            index = 0
            for y in range(height - 1, -1, -1):
                for x in range(width):
                    b = data[index]
                    g = data[index + 1]
                    r = data[index + 2]
                    image_array[y, x] = [b, g, r]
                    index += 3
                index += padding
        except IndexError:
            print("Error: Invalid BMP data.")
            return None
        
        return image_array

    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        height, width, _ = image.shape

        # Calculate the padding for each row
        padding = (4 - (width * 3) % 4) % 4

        # Write the BMP header
        header_size = 54
        image_size = (width * 3 + padding) * height
        file_size = header_size + image_size
        header = struct.pack(
            "<2sI4xI4xIIIIHHIIIIII",
            b"BM", file_size, header_size, 40, width, height, 1, 24, 0, image_size, 0, 0, 0, 0
        )

        # Write the image data
        data = b""
        for y in range(height - 1, -1, -1):
            for x in range(width):
                b, g, r = image[y, x]
                data += struct.pack("BBB", b, g, r)
            data += b"\x00" * padding

        try:
            with open(filepath, "wb") as f:
                f.write(header)
                f.write(data)
            return True
        except IOError:
            print(f"Error: Unable to save file '{filepath}'.")
            return False

class JPEGHandler(AbstractImageHandler):
    def read_image(self, filepath: str) -> np.ndarray:
        try:
            img = Image.open(filepath)
            img_array = np.array(img)
            return img_array
        except IOError as e:
            print(f"Error reading JPEG file: {e}")
            return None

    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        try:
            img = Image.fromarray(image)
            img.save(filepath)
            return True
        except IOError as e:
            print(f"Error writing JPEG file: {e}")
            return False

class PNGHandler(AbstractImageHandler):
    def read_image(self, filepath: str) -> np.ndarray:
        try:
            img = Image.open(filepath)
            img_array = np.array(img)
            return img_array
        except IOError as e:
            print(f"Error reading PNG file: {e}")
            return None

    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        try:
            img = Image.fromarray(image)
            img.save(filepath)
            return True
        except IOError as e:
            print(f"Error writing PNG file: {e}")
            return False

class ImageHandlerFactory:
    handlers = {
        ".bmp": BMPHandler,
        ".jpeg": JPEGHandler,
        ".jpg": JPEGHandler,
        ".png": PNGHandler,
    }

    @staticmethod
    def get_handler(filepath: str) -> AbstractImageHandler:
        file_extension = os.path.splitext(filepath)[1].lower()
        if file_extension in ImageHandlerFactory.handlers:
            return ImageHandlerFactory.handlers[file_extension]()
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
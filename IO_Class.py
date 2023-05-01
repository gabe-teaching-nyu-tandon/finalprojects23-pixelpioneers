import struct
import numpy as np
from abc import ABC, abstractmethod
import os
from PIL import Image, UnidentifiedImageError
import cairosvg
import io

class UnsupportedFileFormatException(Exception):
    pass

class AbstractImageHandler(ABC):
    @abstractmethod
    def read_image(self, filepath: str) -> np.ndarray:
        pass

    @abstractmethod
    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        pass

class CorruptedBMPError(Exception):
    pass

class CorruptedImageDataError(Exception):
    pass

class BMPHandler(AbstractImageHandler):
    def is_valid_image_data(self, image: np.ndarray) -> bool:
        if image is None:
            return False
        if image.ndim != 3 or image.shape[2] != 3:
            return False
        return True
    
    def is_valid_bmp_header(self, header: bytes) -> bool:
        # Check if the BMP header starts with "BM"
        if header[0:2] != b"BM":
            return False

        # Check if the header size is 54 bytes
        header_size = struct.unpack("<I", header[10:14])[0]
        if header_size != 54:
            return False

        return True

    def read_image(self, filepath: str) -> np.ndarray:
        try:
            with open(filepath, 'rb') as f:
                header = f.read(54)
                if not self.is_valid_bmp_header(header):
                    raise CorruptedBMPError()
                width, height, bits_per_pixel = struct.unpack("<3I", header[18:30])
                data = f.read()
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return None
        except IOError:
            print(f"Error: Unable to open file '{filepath}'.")
            return None
        except CorruptedBMPError:
            print("Error: Corrupted BMP file.")
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
        try:
            if not self.is_valid_image_data(image):
                raise CorruptedImageDataError()
            for y in range(height - 1, -1, -1):
                for x in range(width):
                    b, g, r = image[y, x]
                    data += struct.pack("BBB", b, g, r)
                data += b"\x00" * padding

            with open(filepath, "wb") as f:
                f.write(header)
                f.write(data)
            return True
        except IOError:
            print(f"Error: Unable to save file '{filepath}'.")
            return False
        except CorruptedImageDataError:
            print("Error: Corrupted image data.")
            return False

class JPEGHandler(AbstractImageHandler):
    def is_valid_image_data(self, image: np.ndarray) -> bool:
        if image is None:
            return False
        if image.ndim != 3 or image.shape[2] != 3:
            return False
        return True
    
    def read_image(self, filepath: str) -> np.ndarray:
        try:
            img = Image.open(filepath)
            img_array = np.array(img)
            return img_array
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return None
        except UnidentifiedImageError:
            print(f"Error: Corrupted JPEG file.")
            return None
        except IOError as e:
            print(f"Error reading JPEG file: {e}")
            return None

    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        try:
            if not self.is_valid_image_data(image):
                raise CorruptedImageDataError()
            img = Image.fromarray(image)
            img.save(filepath)
            return True
        except IOError as e:
            print(f"Error writing JPEG file: {e}")
            return False
        except CorruptedImageDataError:
            print("Error: Corrupted image data.")
            return False

class PNGHandler(AbstractImageHandler):
    def is_valid_image_data(self, image: np.ndarray) -> bool:
        if image is None:
            return False
        if image.ndim != 3 or image.shape[2] != 3:
            return False
        return True
    
    def read_image(self, filepath: str) -> np.ndarray:
        try:
            img = Image.open(filepath)
            img_array = np.array(img)
            return img_array
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return None
        except UnidentifiedImageError:
            print(f"Error: Corrupted PNG file.")
            return None
        except IOError as e:
            print(f"Error reading PNG file: {e}")
            return None

    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        try:
            if not self.is_valid_image_data(image):
                raise CorruptedImageDataError()
            img = Image.fromarray(image)
            img.save(filepath)
            return True
        except IOError as e:
            print(f"Error writing PNG file: {e}")
            return False
        except CorruptedImageDataError:
            print("Error: Corrupted image data.")
            return False
        
class SVGHandler(AbstractImageHandler):
    def is_valid_image_data(self, image: np.ndarray) -> bool:
        return False
    
    def read_image(self, filepath: str) -> np.ndarray:
        try:
            png_bytes = cairosvg.svg2png(url=filepath)
            img = Image.open(io.BytesIO(png_bytes))
            img_array = np.array(img)
            return img_array
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return None
        except UnidentifiedImageError:
            print(f"Error: Corrupted SVG file.")
            return None
        except Exception as e:
            print(f"Error reading SVG file: {e}")
            return None

    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        try:
            if not self.is_valid_image_data(image):
                raise CorruptedImageDataError()
        except CorruptedImageDataError:
            print("Error: Writing SVG files is not supported. Please convert the image to a supported format (e.g., PNG, JPEG, BMP) before writing.")
        return False

class ImageHandlerFactory:
    handlers = {
        ".bmp": BMPHandler,
        ".jpeg": JPEGHandler,
        ".jpg": JPEGHandler,
        ".png": PNGHandler,
        ".svg": SVGHandler,
    }

    @staticmethod
    def get_handler(filepath: str) -> AbstractImageHandler:
        file_extension = os.path.splitext(filepath)[1].lower()
        if file_extension in ImageHandlerFactory.handlers:
            return ImageHandlerFactory.handlers[file_extension]()
        else:
            raise UnsupportedFileFormatException(f"Unsupported file format: {file_extension}")

class UnifiedImageHandler(AbstractImageHandler):
    def read_image(self, filepath: str) -> np.ndarray:
        try:
            handler = ImageHandlerFactory.get_handler(filepath)
            return handler.read_image(filepath)
        except UnsupportedFileFormatException as e:
            print(e)
            return None

    def write_image(self, filepath: str, image: np.ndarray) -> bool:
        try:
            handler = ImageHandlerFactory.get_handler(filepath)
            return handler.write_image(filepath, image)
        except UnsupportedFileFormatException as e:
            print(e)
            return False
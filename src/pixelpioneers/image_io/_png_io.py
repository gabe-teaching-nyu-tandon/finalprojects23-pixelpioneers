import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

logger = logging.getLogger(__name__)


class PNGHandler(AbstractImageReader, AbstractImageWriter):
    """Handler for reading and writing PNG images.

    This class implements the AbstractImageReader and AbstractImageWriter interfaces
    for reading and writing PNG images, respectively.
    """

    def read(self, path: str) -> np.ndarray:
        """Reads a PNG image from the specified path and returns it as a NumPy array.

        Args:
            path (str): The path to the PNG image file.

        Returns:
            np.ndarray: The image data as a NumPy array.

        Raises:
            ImageIOError: If there is an error reading the image.

        """
        try:
            logger.debug(f"Reading Image from Path -> {path}")
            img = Image.open(path, formats=["png"])
            img_array = np.array(img)
            return img_array

        except FileNotFoundError as fnfe:
            logger.error(f"Error reading image: File '{path}' not found.")
            raise ImageIOError(f"Error reading image: File '{path}' not found.")

        except UnidentifiedImageError as uie:
            logger.error(f"Error reading image: Unrecognized file format.")
            raise ImageIOError(f"Error reading image: Unrecognized file format.")

        except Exception as e:
            logger.error(f"Error reading image: {str(e)}")
            raise ImageIOError

    def write(self, path: str, image: np.ndarray) -> bool:
        """Writes a given NumPy array image to the specified path as a PNG image.

        Args:
            path (str): The path to save the PNG image file.
            image (np.ndarray): The image data as a NumPy array.

        Returns:
            bool: True if the image was successfully written, False otherwise.

        Raises:
            ImageIOError: If there is an error writing the image.

        """
        try:
            logger.debug(f"Writing Image -> {path}")
            img = Image.fromarray(image)
            img.save(path)
            return True

        except IOError as ioe:
            logger.error(f"Error writing image: {str(ioe)}")
            raise ImageIOError(f"Error writing image: {ioe}")

        except Exception as e:
            logger.error(f"Error writing image: {str(e)}")
            raise ImageIOError


if __name__ == "__main__":
    pngHandler = PNGHandler()
    img = pngHandler.read("data/sample.png")
    pngHandler.write("data/sample_out.png", img)

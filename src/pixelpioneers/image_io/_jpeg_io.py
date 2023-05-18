import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

logger = logging.getLogger(__name__)


class JPEGHandler(AbstractImageReader, AbstractImageWriter):
    """
    JPEGHandler is a class that provides methods for reading and writing JPEG images.
    It inherits from AbstractImageReader and AbstractImageWriter.
    """

    def read(self, path: str) -> np.ndarray:
        """
        Read an image from the specified path.

        :param path: The path to the image file.
        :return: A NumPy array representing the image.
        :raises ImageIOError: If there is an error reading the image.
        """
        try:
            logger.debug(f"Reading Image from Path -> {path}")
            img = Image.open(path, formats=["jpeg"])
            img_array = np.array(img)
            return img_array

        except FileNotFoundError as fnfe:
            logger.error(f"Error reading image: File '{path}' not found.")
            raise ImageIOError(f"Error reading image: File '{path}' not found.")

        except UnidentifiedImageError as uie:
            logger.error(f"Error reading image: Unrecognized file format.")
            raise ImageIOError(f"Error reading image: Unrecognized file format.")

        except Exception as e:
            logger.error("Error reading image.")
            raise ImageIOError

    def write(self, path: str, image: np.ndarray) -> bool:
        """
        Write the image to the specified path.

        :param path: The path to save the image file.
        :param image: The NumPy array representing the image.
        :return: True if the image was successfully written, False otherwise.
        :raises ImageIOError: If there is an error writing the image.
        """
        try:
            logger.debug(f"Writing Image -> {path}")
            img = Image.fromarray(image)
            img.save(path)
            logger.debug("Image written successfully.")
            return True

        except IOError as ioe:
            logger.error(f"Error writing image: {ioe}")
            raise ImageIOError(f"Error writing image: {ioe}")

        except Exception as e:
            logger.error("Error writing image.")
            raise ImageIOError


if __name__ == "__main__":
    logger.info("Starting JPEGHandler application.")
    jpegHandler = JPEGHandler()
    img = jpegHandler.read("data/sample.jpeg")
    jpegHandler.write("data/sample_out.jpeg", img)
    logger.info("JPEGHandler application finished.")

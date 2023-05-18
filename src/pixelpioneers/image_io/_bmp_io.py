import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

logger = logging.getLogger(__name__)


class BMPHandler(AbstractImageReader, AbstractImageWriter):
    """
        BMPHandler class implements the AbstractImageReader and AbstractImageWriter interfaces to handle BMP image files.
     """

    def read(self, path: str) -> np.ndarray:
        """
        Read an image from the given path.

        :param str path: Path of the image file to read.
        :return: The RGB image as a numpy ndarray.
        :rtype: np.ndarray
        :raises ImageIOError: If there is an error reading the image.
        """
        try:
            logger.debug(f"Reading Image from Path -> {path}")
            img = Image.open(path, formats=["bmp"])
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
        Write the given RGB image array to a file.

        :param str path: Destination file path to write the image.
        :param np.ndarray image: The RGB image as a numpy ndarray.
        :return: True if the image is successfully written, False otherwise.
        :rtype: bool
        :raises ImageIOError: If there is an error writing the image.
        """
        try:
            logger.debug(f"Writing Image -> {path}")
            img = Image.fromarray(image)
            img.save(path)
            return True

        except IOError as ioe:
            logger.error(f"Error writing image: {ioe}")
            raise ImageIOError(f"Error writing image: {ioe}")

        except Exception as e:
            logger.error("Error writing image.")
            raise ImageIOError


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    bmpHandler = BMPHandler()
    img = bmpHandler.read("data/sample.bmp")
    bmpHandler.write("data/sample_out.bmp", img)

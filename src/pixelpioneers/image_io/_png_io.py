import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

logger = logging.getLogger(__name__)


class PNGHandler(AbstractImageReader, AbstractImageWriter):

    def read(self, path: str) -> np.ndarray:
        try:
            logger.debug(f"Reading Image from Path -> {path}")
            img = Image.open(path, formats=["png"])
            img_array = np.array(img)
            return img_array

        except FileNotFoundError as fnfe:
            raise ImageIOError(f"Error reading image: File '{path}' not found.")

        except UnidentifiedImageError as uie:
            raise ImageIOError(f"Error reading image: Unrecognized file format.")

        except Exception as e:
            raise ImageIOError

    def write(self, path: str, image: np.ndarray) -> bool:
        try:
            logger.debug(f"Writing Image -> {path}")
            img = Image.fromarray(image)
            img.save(path)
            return True

        except IOError as ioe:
            raise ImageIOError(f"Error writing image: {ioe}")

        except Exception as e:
            raise ImageIOError


if __name__ == "__main__":
    pngHandler = PNGHandler()
    img = pngHandler.read("data/sample.png")
    pngHandler.write("data/sample_out.png", img)

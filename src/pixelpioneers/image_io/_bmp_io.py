import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

logger = logging.getLogger(__name__)


class JPEGHandler(AbstractImageReader, AbstractImageWriter):

    def read(self, path: str) -> np.ndarray:
        img = Image.open(path, formats=["jpeg"])
        img_array = np.array(img)
        return img_array


if __name__ == "__main__":
    jpegHandler = JPEGHandler()
    img = jpegHandler.read("data/sample.jpeg")
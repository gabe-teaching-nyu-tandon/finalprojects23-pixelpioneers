import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

class BMPHandler(AbstractImageReader, AbstractImageWriter):
    def read(self, path: str) -> np.ndarray:
        img = Image.open(path, formats=["bmp"])
        img_array = np.array(img)
        return img_array

if __name__ == "__main__":
    bmpHandler = BMPHandler()
    img = bmpHandler.read("data/sample.bmp")
import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

class PNGHandler(AbstractImageReader, AbstractImageWriter):

    def read(self, path: str) -> np.ndarray:
        img = Image.open(path, formats=["png"])
        img_array = np.array(img)
        return img_array
    
    def write(self, path: str, image: np.ndarray) -> bool:
        img = Image.fromarray(image)
        img.save(path)
        return True

if __name__ == "__main__":
    pngHandler = PNGHandler()
    img = pngHandler.read("data/sample.png")
    pngHandler.write("data/sample_out.png", img)
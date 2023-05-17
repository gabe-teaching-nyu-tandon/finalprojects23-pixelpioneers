import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

class JPEGHandler(AbstractImageReader, AbstractImageWriter):
    def read(self, path: str) -> np.ndarray:
        img = Image.open(path, formats=["jpeg"])
        img_array = np.array(img)
        return img_array
    
    def write(self, path: str, image: np.ndarray) -> bool:
        img = Image.fromarray(image)
        img.save(path)
        return True
    
if __name__ == "__main__":
    jpegHandler = JPEGHandler()
    img = jpegHandler.read("data/sample.jpeg")
    jpegHandler.write("data/sample_out.jpeg", img)
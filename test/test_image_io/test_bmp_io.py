import unittest
import os
import numpy as np
from PIL import Image
from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io import BMPHandler

class BMPHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.bmpHandler = BMPHandler()
        self.sample_image_path = "data/sample.bmp"
        self.output_image_path = "data/sample_out.bmp"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_read_existing_image(self):
        img_array = self.bmpHandler.read(self.sample_image_path)
        self.assertIsInstance(img_array, np.ndarray)

    def test_read_nonexistent_image(self):
        with self.assertRaises(ImageIOError):
            self.bmpHandler.read("data/nonexistent.bmp")

    def test_read_unrecognized_format(self):
        with self.assertRaises(ImageIOError):
            self.bmpHandler.read("data/sample.jpg")

    def test_write_image(self):
        img = np.array(Image.open(self.sample_image_path))
        self.assertTrue(self.bmpHandler.write(self.output_image_path, img))
        self.assertTrue(os.path.exists(self.output_image_path))

    def test_write_image_io_error(self):
        with self.assertRaises(ImageIOError):
            self.bmpHandler.write("/invalid/path/sample_out.bmp", np.array([]))

if __name__ == '__main__':
    unittest.main()

import unittest
import os
import numpy as np
from PIL import Image
from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io import JPEGHandler

class JPEGHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.jpegHandler = JPEGHandler()
        self.sample_image_path = "data/sample.jpeg"
        self.output_image_path = "data/sample_out.jpeg"

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_read_existing_image(self):
        img_array = self.jpegHandler.read(self.sample_image_path)
        self.assertIsInstance(img_array, np.ndarray)

    def test_read_nonexistent_image(self):
        with self.assertRaises(ImageIOError):
            self.jpegHandler.read("data/nonexistent.jpeg")

    def test_read_unrecognized_format(self):
        with self.assertRaises(ImageIOError):
            self.jpegHandler.read("data/sample.jpg")

    def test_write_image(self):
        img = np.array(Image.open(self.sample_image_path))
        self.assertTrue(self.jpegHandler.write(self.output_image_path, img))
        self.assertTrue(os.path.exists(self.output_image_path))

    def test_write_image_io_error(self):
        with self.assertRaises(ImageIOError):
            self.jpegHandler.write("/invalid/path/sample_out.jpeg", np.array([]))

if __name__ == '__main__':
    unittest.main()

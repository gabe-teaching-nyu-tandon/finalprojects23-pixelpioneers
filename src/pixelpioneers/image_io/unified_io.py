import logging
from pathlib import Path

import numpy as np

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io import BMPHandler, PNGHandler, JPEGHandler

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class UnifiedIO:
    """Class for unified image input/output operations."""
    io_handlers = {
        ".bmp": BMPHandler(),
        ".png": PNGHandler(),
        ".jpeg": JPEGHandler()
    }

    @staticmethod
    def read(path: str) -> np.ndarray:
        """Read an image file.

        Args:
            path (str): The path to the image file.

        Returns:
            np.ndarray: The image data as a NumPy array.

        Raises:
            ImageIOError: If there was an error reading the image.
        """
        try:
            path = Path(path)
            assert path.is_file(), "Expected path to a File"
            logger.debug(f"Reading image from path: {path}")

            file_ext = path.suffix
            assert file_ext in UnifiedIO.io_handlers, f"Unsupported File Format: {file_ext}"
            logger.debug(f"Detected file format: {file_ext}")

            io_handler = UnifiedIO.io_handlers[file_ext]
            logger.debug("Image read successfully")
            return io_handler.read(path)

        except AssertionError as ae:
            logger.exception(f"Error reading image: {ae}")
            raise ImageIOError(f"Error reading image: {ae}")

    @staticmethod
    def write(path: str, image: np.ndarray) -> bool:
        """Write an image to a file.

        Args:
            path (str): The path to write the image file.
            image (np.ndarray): The image data as a NumPy array.

        Returns:
            bool: True if the image was successfully written, False otherwise.

        Raises:
            ImageIOError: If there was an error writing the image.
        """
        try:

            path = Path(path)
            file_ext = path.suffix
            assert file_ext in UnifiedIO.io_handlers, f"Unsupported File Format: {file_ext}"
            logger.debug(f"Writing image to path: {path}")

            if not path.parent.exists():
                path.parent.mkdir(parents=True)
                logger.debug(f"Created directory: {path.parent}")

            io_handler = UnifiedIO.io_handlers[file_ext]
            return io_handler.write(path, image)

        except AssertionError as ae:
            logger.exception(f"Error writing image: {ae}")
            raise ImageIOError(f"Error reading image: {ae}")

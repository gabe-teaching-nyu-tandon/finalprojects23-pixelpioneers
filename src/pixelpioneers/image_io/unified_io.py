from pathlib import Path

import numpy as np

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io import BMPHandler, PNGHandler, JPEGHandler


class UnifiedIO:
    io_handlers = {
        ".bmp": BMPHandler(),
        ".png": PNGHandler(),
        ".jpeg": JPEGHandler()
    }

    @staticmethod
    def read(path: str) -> np.ndarray:
        try:

            path = Path(path)
            assert path.is_file(), "Expected path to a File"

            file_ext = path.suffix
            assert file_ext in UnifiedIO.io_handlers, f"Unsupported File Format: {file_ext}"

            io_handler = UnifiedIO.io_handlers[file_ext]
            return io_handler.read(path)

        except AssertionError as ae:
            raise ImageIOError(f"Error reading image: {ae}")

    @staticmethod
    def write(path: str, image: np.ndarray) -> bool:

        try:

            path = Path(path)
            file_ext = path.suffix
            assert file_ext in UnifiedIO.io_handlers, f"Unsupported File Format: {file_ext}"

            if not path.parent.exists():
                path.parent.mkdir(parents=True)

            io_handler = UnifiedIO.io_handlers[file_ext]
            return io_handler.write(path, image)

        except AssertionError as ae:
            raise ImageIOError(f"Error reading image: {ae}")

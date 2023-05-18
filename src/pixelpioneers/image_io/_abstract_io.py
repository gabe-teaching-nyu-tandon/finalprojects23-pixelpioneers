from abc import ABC, abstractmethod

import numpy as np


class AbstractImageReader(ABC):
    """
    Abstract Image Reader Class
    """

    def __init__(self):
        pass

    @abstractmethod
    def read(self, path: str) -> np.ndarray:
        """
        Function to read an image
        :param str path: path of file to read
        :return: np.ndarray - RGB image
        :
        """
        pass


class AbstractImageWriter(ABC):
    """
    Abstract Image Writer Class
    """

    def __init__(self):
        pass

    @abstractmethod
    def write(self, path: str, image: np.ndarray) -> bool:
        """
        Function used to write a given RGB array to file
        :param str path: destination file path
        :param np.ndarray image: RGB image array
        :return:
        """
        pass

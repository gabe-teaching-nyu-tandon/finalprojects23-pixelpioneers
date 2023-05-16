from abc import ABC

import numpy as np


class AbstractImageAction(ABC):
    name = "AbstractImageAction"

    def __init__(self):
        pass

    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        pass

    @staticmethod
    def get_actions():
        pass

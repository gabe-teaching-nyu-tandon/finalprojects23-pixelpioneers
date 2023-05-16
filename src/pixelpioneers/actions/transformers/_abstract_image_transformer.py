from abc import abstractmethod

import numpy as np

from pixelpioneers.actions.abstract_image_action import AbstractImageAction


class AbstractImageTransformer(AbstractImageAction):
    name = super.name + "AbstractImageTransformer"

    def __init__(self):
        super(AbstractImageTransformer, self).__init__()

    @abstractmethod
    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        pass

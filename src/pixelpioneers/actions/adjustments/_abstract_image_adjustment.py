from abc import abstractmethod

import numpy as np

from pixelpioneers.actions.abstract_image_action import AbstractImageAction


class AbstractImageAdjustment(AbstractImageAction):
    name = super.name + "AbstractImageAdjustment"

    def __init__(self):
        super(AbstractImageAdjustment, self).__init__()

    @abstractmethod
    def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
        pass

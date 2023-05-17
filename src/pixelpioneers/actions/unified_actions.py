from pixelpioneers.actions.abstract_image_action import AbstractImageAction
from pixelpioneers.actions.adjustments import *
from pixelpioneers.actions.transformers import *
from pixelpioneers.exceptions import ActionError


class UnifiedActions:
    actions = {
        "brightness": BrightnessAdjustment,
        "contrast": ContrastAdjustment,
        "saturation": SaturationAdjustment,
        "crop": CropTransformer,
        "flip": FlipTransformer,
        "grayscale": GrayscaleTransformer,
        "invert": InvertTransformer,
        "resize": ResizeTransformer,
        "rotate": RotateTransformer
    }

    @staticmethod
    def get_action_instance(action: str, action_args: dict) -> AbstractImageAction:
        try:

            assert action in UnifiedActions.actions, f"Unsupported Action - {action}"

            action_cls = UnifiedActions.actions[action]
            return action_cls(**action_args)

        except AssertionError as ae:
            raise ActionError(f"Action Error: {ae}")

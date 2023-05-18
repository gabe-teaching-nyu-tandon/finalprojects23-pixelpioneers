class ImageIOError(Exception):

    def __init__(self, message: str = "ImageIO Error: Unknown Exception"):
        super(ImageIOError, self).__init__(message)


class ActionError(Exception):
    def __init__(self, message: str = "Action Error: Unknown Exception"):
        super(ActionError, self).__init__(message)


class ImageAdjustmentError(ActionError):

    def __init__(self, message: str = "Image Adjustment Error: Unknown Exception"):
        super(ImageAdjustmentError, self).__init__(message)


class ImageTransformationError(ActionError):

    def __init__(self, message: str = "Image Transformation Error: Unknown Exception"):
        super(ImageTransformationError, self).__init__(message)

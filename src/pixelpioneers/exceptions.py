class ImageIOError(Exception):

    def __init__(self, message: str = "ImageIO Error: Unknown Exception"):
        super(ImageIOError, self).__init__(message)


class ImageAdjustmentError(Exception):

    def __init__(self, message: str = "Image Adjustment Error: Unknown Exception"):
        super(ImageAdjustmentError, self).__init__(message)


class ImageTransformationError(Exception):

    def __init__(self, message: str = "Image Transformation Error: Unknown Exception"):
        super(ImageTransformationError, self).__init__(message)

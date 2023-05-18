def __init__(self):
    super(GrayscaleTransformer, self).__init__()

def apply(self, image: np.ndarray, *args, **kwargs) -> np.ndarray:
    assert image is not None, "Function parameter image: cannot be None"
    assert image.ndim == 3, f"Expected a 3 dimensional image, Instead got a image with {image.ndim} dimensions"

    return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
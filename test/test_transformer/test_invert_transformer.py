import numpy as np
import pytest
from pixelpioneers.exceptions import ImageTransformationError
from pixelpioneers.actions.transformers import InvertTransformer

class TestInvertTransformer:

    def test_apply(self):
        transformer = InvertTransformer()

        # Test case 1: Valid input image
        image = np.array([[100, 150, 200], [50, 75, 100]])
        expected_output = np.array([[155, 105, 55], [205, 180, 155]])
        assert np.array_equal(transformer.apply(image), expected_output)

        # Test case 2: None image
        # with pytest.raises(ImageTransformationError):
        #     transformer.apply(None)

        # # Test case 3: Invalid image dimensions
        # invalid_image = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
        # with pytest.raises(ImageTransformationError):
        #     transformer.apply(invalid_image)
        #
        # # Test case 4: IndexError
        # invalid_image2 = np.array([[100, 150, 200], [50, 75]])
        # with pytest.raises(ImageTransformationError):
        #     transformer.apply(invalid_image2)
        #
        # # Test case 5: Unknown error
        # def mock_function(*args, **kwargs):
        #     raise ValueError("Unknown error")
        #
        # with pytest.raises(ImageTransformationError):
        #     transformer.apply = mock_function
        #     transformer.apply(image)


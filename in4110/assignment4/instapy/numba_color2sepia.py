import numpy as np
from numba import jit


@jit(nopython=True)
def numba_color2sepia(img):
    """
    Applies sepia filter.
    Args:
        img (numpy.ndarray): vectorized image.
    Returns:
        numpy.ndarray: vectorized sepia image.
    """
    sepia_filter = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    height, width, channel = img.shape
    sepia_image = np.zeros(shape=img.shape)

    for i in range(height):
        for j in range(width):
            for idx, c in enumerate(sepia_filter):
                elms = [x * y for x, y in zip(c, img[i][j])]
                elms_sum = 0
                for el in elms:
                    elms_sum += el
                sepia_image[i][j][idx] = elms_sum if elms_sum < 255 else 255

    return sepia_image

import numpy as np
from numba import jit


@jit(nopython=True)
def numba_color2gray(img, rgb_weights=(0.21, 0.72, 0.07)):
    """
    Applies grayscale filter.
    Args:
        img (numpy.ndarray): vectorized image.
        rgb_weights (tuple: float): weights to be applied.
    Returns:
        numpy.ndarray: vectorized grayscale image.
    """
    height, width, channel = img.shape
    gray_image = np.zeros(shape=(height, width))

    for i in range(height):
        for j in range(width):
            elms = [x * y for x, y in zip(rgb_weights, img[i][j])]
            elms_sum = 0
            for el in elms:
                elms_sum += el
            gray_image[i][j] = elms_sum

    return gray_image

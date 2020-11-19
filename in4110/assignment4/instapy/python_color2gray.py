import numpy as np


def python_color2gray(img, rgb_weights=(0.21, 0.72, 0.07)):
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
            gray_image[i][j] = sum(x * y for x, y in zip(rgb_weights, img[i][j]))

    return gray_image

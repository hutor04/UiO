import numpy as np


def numpy_color2gray(img, rgb_weights=(0.21, 0.72, 0.07)):
    """
    Applies grayscale filter.
    Args:
        img (numpy.ndarray): vectorized image.
        rgb_weights (tuple: float): weights to be applied.
    Returns:
        numpy.ndarray: vectorized grayscale image.
    """
    gray_image = np.dot(img[..., :3], rgb_weights)
    return gray_image

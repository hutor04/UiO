import numpy as np


def numpy_color2sepia(img):
    """
    Applies sepia filter.
    Args:
        img (numpy.ndarray): vectorized image.
    Returns:
        numpy.ndarray: vectorized sepia image.
    """
    sepia_matrix = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
    sepia_image = img.dot(sepia_matrix.T)
    sepia_image = np.where(sepia_image > 255, 255, sepia_image)
    return sepia_image

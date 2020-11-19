import cv2
import numpy as np


def read_file(path):
    """
    Reads and vectorizes image from path.
    Args:
        path (str): Path to the input file.
    Returns:
        numpy.ndarray: Vectorized image.
    """
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image.astype(np.double)


def write_file(path, data):
    """
    Converts vectorized image to the format specified in the extension and saves to the specified file.
    Args:
        path (str): Path to the output file.
        data (numpy.ndarray): Vectorized image.
    Returns:
        None
    """
    output = data.astype('uint8')
    output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, output)

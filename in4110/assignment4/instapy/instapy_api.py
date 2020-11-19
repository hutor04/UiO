import cv2
import numpy
from instapy.file_rw import read_file, write_file
from instapy.python_color2gray import python_color2gray
from instapy.numpy_color2gray import numpy_color2gray
from instapy.numba_color2gray import numba_color2gray
from instapy.cython_color2gray import cython_color2gray
from instapy.python_color2sepia import python_color2sepia
from instapy.numpy_color2sepia import numpy_color2sepia
from instapy.numba_color2sepia import numba_color2sepia
from instapy.cython_color2sepia import cython_color2sepia


def grayscale_image(input_filename, output_filename=None, impl='numpy', scale='1'):
    """
    Applies grayscale filter using specified implementation. Saves the result to file if provided or returns
    vectorized image.
    Args:
        input_filename (str): path to input file.
        output_filename (str): path to output file.
        impl (str): implemantation: [numpy, python, numba, cython].
        scale (float): Scaling factor for rescaling the image. scale = 1 gives no scaling. Default is 1.
    Returns:
        None or numpy.ndarray: grayscale image.
    """
    implementations = {'python': python_color2gray, 'numpy': numpy_color2gray, 'numba': numba_color2gray,
                       'cython': cython_color2gray}
    img = read_file(input_filename).astype(numpy.double)
    img = cv2.resize(img, (0,0), fx = scale, fy = scale)
    gray = implementations[impl](img)
    if output_filename is not None:
        write_file(output_filename, gray)
    return gray


def sepia_image(input_filename, output_filename=None, impl='numpy', scale='1'):
    """
    Applies sepia filter using specified implementation. Saves the result to file if provided or returns
    vectorized image.
    Args:
        input_filename (str): path to input file.
        output_filename (str): path to output file.
        impl (str): implemantation: [numpy, python, numba, cython].
        scale (float): Scaling factor for rescaling the image. scale = 1 gives no scaling. Default is 1.
    Returns:
        None or numpy.ndarray: sepia image.
    """
    implementations = {'python': python_color2sepia, 'numpy': numpy_color2sepia, 'numba': numba_color2sepia,
                       'cython': cython_color2sepia}
    img = read_file(input_filename)
    img = cv2.resize(img, (0,0), fx = scale, fy = scale)
    sepia = implementations[impl](img)
    if output_filename is not None:
        write_file(output_filename, sepia)
    output = cv2.cvtColor(sepia, cv2.COLOR_RGB2BGR)
    return output

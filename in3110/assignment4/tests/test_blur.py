#!/usr/bin/env python3

import numpy as np
import cv2
import time
from blurring3110 import blur_1
from blurring3110 import blur_2
from blurring3110 import blur_3
import pytest


def blur_image(input_filename, output_filename=None):
    """
    Converts an input image into a blurred image. If output filename is supplied,
    the blurred image should also be saved to the specified location. The underlying function is NumPy based.
    :param input_filename: str
                        Path to the input image file.
    :param output_filename: str
                        Path to the input image file.
    :return: numpy.ndarray
                        Unsigned integer 3D array of a blurred image.

    """
    if output_filename is not None:
        return blur_2.convert_np(input_filename, output_filename).astype("uint8")
    else:
        image = cv2.imread(input_filename)
        return blur_2.convolution_average_np(image)


def _generate_arr():
    """
    Helper that creates 3D array for testing
    :return: numpy.ndarray
                        3D array of integers.
    """
    np.random.seed(1)
    return np.random.randint(low=0, high=256, size=(3, 3, 3))


def test_check_max():
    """
    Testing if max value in the arrays reduces.
    :return: None
    """
    test_arr = _generate_arr()
    test_max = np.amax(test_arr)

    out_py = blur_1.convolution_average(test_arr)
    assert np.amax(out_py) < test_max

    out_numpy = blur_2.convolution_average_np(test_arr)
    assert np.amax(out_numpy) < test_max

    test_w_pad = np.pad(test_arr, [(1, 1), (1, 1), (0, 0)], mode='edge')
    out_numba = blur_3.convolution_average_numba(test_w_pad).astype("uint8")
    assert np.amax(out_numba) < test_max


def test_pixel_average():
    """
    Testing if the average of neighbouring pixels is calculated correctly.
    :return: None
    """
    test_arr = _generate_arr()
    test_avg = 154

    out_py = blur_1.convolution_average(test_arr).astype("uint8")
    assert out_py[1, 1, 1] == test_avg

    out_numpy = blur_2.convolution_average_np(test_arr).astype("uint8")
    assert out_numpy[1, 1, 1] == test_avg

    test_w_pad = np.pad(test_arr, [(1, 1), (1, 1), (0, 0)], mode='edge')
    out_numba = blur_3.convolution_average_numba(test_w_pad).astype("uint8")
    assert out_numba[1, 1, 1] == test_avg


def check_speed(function, image, out):
    """
    Helper function that used to check the runtime of convolutions functions.
    :param function: one of the convolution functions.
    :param image: str
                Path to the input image file.
    :param out: str
                Path to the output image file.
    :return: None
    """
    s = time.time()
    function(image, out)
    e = time.time()
    print(f'{function.__name__} runs in {(e - s):.4f}')


if __name__ == '__main__':

    pytest.main()
    IMAGE = '../data/beatles.jpg'
    IMAGE_OUT = '../data/blurred_image.jpg'

    #  Numba is run 2 times on purpose
    funcs = [blur_1.convert_py, blur_2.convert_np, blur_3.convert_nb, blur_3.convert_nb]

    for f in funcs:
        check_speed(f, IMAGE, IMAGE_OUT)

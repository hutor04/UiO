import cv2
import numpy as np


def convolution_average_np(arr):
    """
    The function blurs an image by applying by applying convolution with
    an averaging kernel.

    :param arr: numpy.ndarray
                3-dimensional numpy array with channels C = 3
    :return: numpy.ndarray
             3-dimensional numpy array with channels C = 3
    """
    src = np.pad(arr, [(1, 1), (1, 1), (0, 0)], mode='edge')

    m1 = src[0:-2, 0:-2, :]
    m2 = src[0:-2, 1:-1, :]
    m3 = src[0:-2, 2:, :]
    m4 = src[1:-1, 0:-2, :]
    m5 = src[1:-1, 2:, :]
    m6 = src[2:, 0:-2, :]
    m7 = src[2:, 1:-1, :]
    m8 = src[2:, 2:, :]

    result = (arr + m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8) / 9

    return result.astype('uint8')


def convert_np(in_file, out_file):
    """
    Applies blur filter to the provided image file and saves the result to the ouput file.
    :param in_file: string
                    Path to the input file.
    :param out_file: string
                    Path to the output file.
    :return: None
    """
    image = cv2.imread(in_file)
    image = image.astype("uint32")
    dst = convolution_average_np(image)
    cv2.imwrite(out_file, dst)

    return dst


if __name__ == '__main__':
    convert_np('../data/beatles.jpg', '../data/blurred_image.jpg')


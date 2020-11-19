import cv2
import numpy as np


def convolution_average(arr):
    """
    The function blurs an image by applying by applying convolution with
    an averaging kernel.
    Note casting to int is done to avoid using operations as defined by NumPy.

    :param arr: numpy.ndarray
                3-dimensional numpy array with channels C = 3
    :return: numpy.ndarray
                3-dimensional numpy array with channels C = 3
    """
    src = np.pad(arr, [(1, 1), (1, 1), (0, 0)], mode='edge')
    dst = np.zeros(shape=arr.shape)
    height, width, channel = arr.shape

    for h in range(1, height):
        for w in range(1, width):
            for c in range(channel):
                dst[h - 1, w - 1, c] = (int(src[h, w, c]) + int(src[h-1, w, c]) + int(src[h+1, w, c])
                                        + int(src[h, w-1, c]) + int(src[h, w+1, c])
                                        + int(src[h-1, w-1, c]) + int(src[h-1, w+1, c])
                                        + int(src[h+1, w-1, c]) + int(src[h+1, w+1, c]))/9

    return dst.astype('uint8')


def convert_py(in_file, out_file):
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
    dst = convolution_average(image)
    cv2.imwrite(out_file, dst)
    return dst


if __name__ == '__main__':
    convert_py('../data/beatles.jpg', '../data/blurred_image.jpg')


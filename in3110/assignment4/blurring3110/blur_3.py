import cv2
import numpy as np
from numba import jit


@jit
def convolution_average_numba(src):
    """
    The function blurs an image by applying by applying convolution with
    an averaging kernel using numpy with numba.
    :param src: numpy.ndarray
                3-dimensional numpy array with channels C = 3
    :return: numpy.ndarray
                3-dimensional numpy array with channels C = 3
    """
    arr = src[1:-1, 1:-1, :]

    m1 = src[0:-2, 0:-2, :]
    m2 = src[0:-2, 1:-1, :]
    m3 = src[0:-2, 2:, :]
    m4 = src[1:-1, 0:-2, :]
    m5 = src[1:-1, 2:, :]
    m6 = src[2:, 0:-2, :]
    m7 = src[2:, 1:-1, :]
    m8 = src[2:, 2:, :]

    result = (arr + m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8) / 9

    return result


@jit
def convolution_average_numba_py(src):
    """
    The function blurs an image by applying by applying convolution with
    an averaging kernel using pure python with numba.
    :param src: numpy.ndarray
                3-dimensional numpy array with channels C = 3
    :return: numpy.ndarray
                3-dimensional numpy array with channels C = 3
    """
    height, width, channel = src.shape
    height -= 2
    width -= 2

    dst = np.zeros(shape=(height, width, channel))

    for h in range(height):
        i = h
        h += 1   # This is used to take care of padding
        for w in range(width):
            j = w
            w += 1   # This is used to take care of padding
            for c in range(channel):
                dst[i, j, c] = (src[h, w, c] + src[h-1, w, c] + src[h+1, w, c]
                                + src[h, w-1, c] + src[h, w+1, c]
                                + src[h-1, w-1, c] + src[h-1, w+1, c]
                                + src[h+1, w-1, c] + src[h+1, w+1, c])/9

    return dst


def convert_nb(in_file, out_file):
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
    src = np.pad(image, [(1, 1), (1, 1), (0, 0)], mode='edge')  # Padding is applied. To support Numba.
    dst = convolution_average_numba_py(src)
    dst = dst.astype('uint8')
    cv2.imwrite(out_file, dst)


if __name__ == '__main__':
    convert_nb('../data/beatles.jpg', '../data/blurred_image.jpg')

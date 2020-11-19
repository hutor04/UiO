import cv2
from blurring3110 import blur_2


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


if __name__ == '__main__':
    blur_image('../data/beatles.jpg', '../data/blurred_image.jpg')

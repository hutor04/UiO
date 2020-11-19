#!/usr/bin/env python3
import pytest
import os
from instapy.python_color2gray import python_color2gray
from instapy.numpy_color2gray import numpy_color2gray
from instapy.numba_color2gray import numba_color2gray
from instapy.cython_color2gray import cython_color2gray
from instapy.python_color2sepia import python_color2sepia
from instapy.numpy_color2sepia import numpy_color2sepia
from instapy.numba_color2sepia import numba_color2sepia
from instapy.cython_color2sepia import cython_color2sepia
from instapy.file_rw import read_file, write_file

source_img_path = '../data/rain.jpg'
unchanged_img_path = '../data/rain_dup.jpg'
gray_img_path = '../data/rain_gray.jpg'
sepia_img_path = '../data/rain_sepia.jpg'

color_image_shape = (400, 600, 3)
gray_image_shape = (400, 600)
pixel_1 = [63, 144, 251]
gray_pixel_1 = 134
sepia_pixel_1 = [182, 162, 126]


class TestFileRW:
    """
    Tests read-write operations.
    """
    def test_file_read(self):
        input_file = read_file(source_img_path)
        assert input_file.shape == color_image_shape

    def test_color_channels_read(self):
        input_file = read_file(source_img_path)
        assert list(input_file[0, 0, :]) == pixel_1

    def test_file_write(self):
        input_file = read_file(source_img_path)
        write_file(unchanged_img_path, input_file)
        assert os.path.isfile(unchanged_img_path)


class TestIstapyColor2gray:
    """
    Tests the implementations of grayscale filter.
    """
    def test_python_dimensions(self):
        input_file = read_file(source_img_path)
        output = python_color2gray(input_file).astype('uint8')
        assert output.shape == gray_image_shape

    def test_numpy_dimensions(self):
        input_file = read_file(source_img_path)
        output = numpy_color2gray(input_file).astype('uint8')
        assert output.shape == gray_image_shape

    def test_numba_dimensions(self):
        input_file = read_file(source_img_path)
        output = numba_color2gray(input_file).astype('uint8')
        assert output.shape == gray_image_shape

    def test_cython_dimensions(self):
        input_file = read_file(source_img_path)
        output = cython_color2gray(input_file).astype('uint8')
        assert output.shape == gray_image_shape

    def test_python_conversion(self):
        input_file = read_file(source_img_path)
        output = python_color2gray(input_file).astype('uint8')
        assert output[0, 0] == gray_pixel_1

    def test_numpy_conversion(self):
        input_file = read_file(source_img_path)
        output = numpy_color2gray(input_file).astype('uint8')
        assert output[0, 0] == gray_pixel_1

    def test_numba_conversion(self):
        input_file = read_file(source_img_path)
        output = numba_color2gray(input_file).astype('uint8')
        assert output[0, 0] == gray_pixel_1

    def test_cython_conversion(self):
        input_file = read_file(source_img_path)
        output = cython_color2gray(input_file).astype('uint8')
        assert output[0, 0] == gray_pixel_1


class TestIstapyColor2sepia:
    """
    Tests the implementations of sepia filter.
    """
    def test_python_dimensions(self):
        input_file = read_file(source_img_path)
        output = python_color2sepia(input_file).astype('uint8')
        assert output.shape == color_image_shape

    def test_numpy_dimensions(self):
        input_file = read_file(source_img_path)
        output = numpy_color2sepia(input_file).astype('uint8')
        assert output.shape == color_image_shape

    def test_numba_dimensions(self):
        input_file = read_file(source_img_path)
        output = numba_color2sepia(input_file).astype('uint8')
        assert output.shape == color_image_shape

    def test_cython_dimensions(self):
        input_file = read_file(source_img_path)
        output = cython_color2sepia(input_file).astype('uint8')
        assert output.shape == color_image_shape

    def test_python_conversion(self):
        input_file = read_file(source_img_path)
        output = python_color2sepia(input_file).astype('uint8')
        assert list(output[0, 0]) == sepia_pixel_1

    def test_numpy_conversion(self):
        input_file = read_file(source_img_path)
        output = numpy_color2sepia(input_file).astype('uint8')
        assert list(output[0, 0]) == sepia_pixel_1

    def test_numba_conversion(self):
        input_file = read_file(source_img_path)
        output = numba_color2sepia(input_file).astype('uint8')
        assert list(output[0, 0]) == sepia_pixel_1

    def test_cython_conversion(self):
        input_file = read_file(source_img_path)
        output = cython_color2sepia(input_file).astype('uint8')
        assert list(output[0, 0]) == sepia_pixel_1


if __name__ == '__main__':
    pytest.main()

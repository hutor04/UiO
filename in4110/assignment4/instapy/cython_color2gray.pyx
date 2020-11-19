import numpy
cimport numpy


cpdef numpy.ndarray[numpy.double_t, ndim=2] cython_color2gray(double[:, :, :] img):
    """
    Applies grayscale filter.
    Args:
        img (double[:, :, :]): vectorized image.
    Returns:
        numpy.ndarray[numpy.double_t, ndim=2]: vectorized grayscale image. 
    """
    cdef int height
    cdef int width
    cdef int channel
    height = len(img)
    width = len(img[0])
    channel = len(img[0][0])

    cdef int i
    cdef int j
    cdef int c
    cdef float channel_sum
    cdef numpy.ndarray[numpy.double_t, ndim=2] out
    out = numpy.ndarray((height, width), dtype=numpy.double)
    cdef list rgb_weights = [0.21, 0.72, 0.07]

    for i in range(height):
        for j in range(width):
            channel_sum = 0
            for c in range(channel):
                channel_sum += img[i][j][c] * rgb_weights[c]
            out[i][j] = channel_sum

    return out

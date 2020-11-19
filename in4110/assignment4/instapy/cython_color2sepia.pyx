import numpy
cimport numpy


cpdef numpy.ndarray[numpy.double_t, ndim=3] cython_color2sepia(double[:, :, :] img):
    """
    Applies sepia filter.
    Args:
        img (double[:, :, :]): vectorized image.
    Returns:
        numpy.ndarray[numpy.double_t, ndim=2]: vectorized sepia image. 
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
    cdef numpy.ndarray[numpy.double_t, ndim=3] out
    out = numpy.zeros(shape=(height, width, channel))
    cdef list sepia_filter = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]

    for i in range(height):
        for j in range(width):
            channel_sum = 0
            for c in range(channel):
                channel_sum = img[i][j][0] * sepia_filter[c][0] + img[i][j][1] * sepia_filter[c][1] +\
                              img[i][j][2] * sepia_filter[c][2]
                out[i][j][c] = channel_sum if channel_sum < 255 else 255

    return out
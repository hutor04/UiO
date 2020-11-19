#!/usr/bin/env python3

import cv2
import numpy as np
from blurring3110 import blur_2


def main(input_file, output_file, model, blurring=40):
    """
    The function takes an image, finds faces on it, then blurs faces and tries to find them again.
    It prints out the number og faces found on an un-blurred image and on blurred.
    :param input_file: str
                        Path to input image file
    :param output_file: str
                        Path to output image file
    :param model: str
                        Path to the model used for face recognition.
    :param blurring: int
                        Number of times the image is re-blurred.
    :return: None
    """

    face_cascade = cv2.CascadeClassifier(model)
    image = cv2.imread(input_file)  # Original image
    blurred = np.copy(image).astype("uint32")  # Blurred faces

    faces = face_cascade.detectMultiScale(image, scaleFactor=1.025, minNeighbors=5, minSize=(30, 30))
    print('Found {} faces on original image!'.format(len(faces)))

    for i, (x, y, w, h) in enumerate(faces):
        face = image[y:y + h, x:x + w]

        for _ in range(blurring):
            face = blur_2.convolution_average_np(face.astype("uint32"))

        blurred[y:y + h, x:x + w] = face

    blurred = blurred.astype('uint8')

    faces_b = face_cascade.detectMultiScale(blurred, scaleFactor=1.025, minNeighbors=5, minSize=(30, 30))
    print("Found {} faces on blurred image!".format(len(faces_b)))

    for (x, y, w, h) in faces_b:
        cv2.rectangle(blurred, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite(output_file, blurred)


if __name__ == '__main__':
    main('../data/beatles.jpg', '../data/faces_blurred.jpg', '../data/haarcascade_frontalface_default.xml')

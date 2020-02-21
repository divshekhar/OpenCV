import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def sketch(image):
    # Convert image to gray scale
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Clean up image using Gaussian Blur
    img_gray_blur = cv.GaussianBlur(img_gray, (5, 5), 0)

    # Extract Edges
    canny_edges = cv.Canny(img_gray_blur, 30, 70)

    # Do an invert binarize the image
    ret, mask = cv.threshold(canny_edges, 120, 255, cv.THRESH_BINARY_INV)

    return mask


def liveSketch():
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv.imshow("Live Sketch", sketch(frame))
        if cv.waitKey(1) == 27:
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    liveSketch()

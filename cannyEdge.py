import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def canny():
    '''
    The Canny edge detection algorithm is composed
                      of 5 steps:

    1. Noise Reduction
    2. Gradient Calculation
    3. Non-maximum Suppressions
    4. Double threshold
    5. Edge Tracking by Hysteresis
    '''
    img = cv.imread("./img/sunflower.jpg", 0)
    canny = cv.Canny(img, 150, 200)

    title = ["Original Image", "Canny"]
    images = [img, canny]

    for i in range(len(images)):
        plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
        plt.title(title[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == '__main__':
    canny()

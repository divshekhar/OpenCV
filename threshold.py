import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def threshold():
    # Read images
    img = cv.imread('./img/gradient.jpg')
    img2 = cv.imread('./img/sudoku.jpg')

    _, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    _, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
    _, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
    _, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
    _, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

    titles = ['Original Image', 'Binary', 'Binary Inverse',
              'Trunc', 'TOZero', 'TOZero Inverse']
    images = [img, th1, th2, th3, th4, th5]

    for i in range(len(images)):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        # TO remove ticks from x and y axis
        plt.xticks([]), plt.yticks([])
    # Adaptive threshold

    # th6 = cv.adaptiveThreshold(
    #     img2, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    # th7 = cv.adaptiveThreshold(
    #     img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

    # adaptiveTitle = ["Original Image", "ADAPTIVE MEAN", "ADAPTIVE GAUSS"]
    # adaptiveImages = [img2, th6, th7]

    # for i in range(len(adaptiveImages)):
    #     plt.subplot(1, 3, i+1)
    #     plt.imshow(adaptiveImages[i], 'gray')
    #     plt.title(adaptiveTitle[i])
    #     # TO remove ticks from x and y axis
    #     plt.xticks([]), plt.yticks([])

    # cv.imshow('Image', img2)
    # cv.imshow('Binary', th1)
    # cv.imshow('Binary Inverse', th2)
    # cv.imshow('Trunc', th3)
    # cv.imshow('TOZero', th4)
    # cv.imshow('TOZero Inverse', th5)

    # cv.imshow("ADAPTIVE MEAN", th6)
    # cv.imshow("ADAPTIVE GAUSS", th7)

    plt.show()

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    threshold()

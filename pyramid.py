import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Image Pyramids


def pyramid():
    '''
    Pyramid, or pyramid representation, is a type of multi-scale signal
    representation in which a signal or an image is subject to repeated
    smoothing and subsampling.
    lr- lower Resolution
    hr- Higher Resolution 

    '''
    img = cv.imread('./img/balls.jpg')
    lr = cv.pyrDown(img)
    # lr2 = cv.pyrDown(lr)

    hr = cv.pyrUp(lr)

    cv.imshow('Original Image', img)
    cv.imshow('PYR DOWN', lr)
    # cv.imshow('PYR DOWN2', lr2)
    cv.imshow('PYR UP', hr)

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    pyramid()

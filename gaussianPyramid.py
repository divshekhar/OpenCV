import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def gaussianPyramid():
    '''
    A level in laplacian Pyramid is formed by the difference
    between that level in Gaussian Pyramid and expanded version 
    of its upper lavel in Gaussian Pyramid.
    '''
    img = cv.imread('./img/balls.jpg')
    layer = img.copy()
    gp = [layer]

    for i in range(1):
        layer = cv.pyrDown(layer)
        gp.append(layer)
        # cv.imshow(str(i), layer)

    layer = gp[len(gp)-1]
    lp = [layer]
    cv.imshow('Last Gaussian Image', layer)

    for i in range(len(gp)-1, 0, -1):
        gaussian_extended = cv.pyrUp(gp[i])
        laplacian = cv.subtract(gp[i-1], gaussian_extended)
        cv.imshow(str(i), laplacian)

    cv.imshow("Original Image", img)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    gaussianPyramid()

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def hough():
    '''
    The Hough Transform is a Popular technique
    to detect any shape, if you can represent
    that shape in a mathematical form, It can
    detect the shape even if it is broken or 
    distorted a little bit.

    # Θ Theta

    A line in the image space can be expressed 
    with two variables.
    For ex:
        -In Cartesian Coordinate System
                    y = mx + c
        -In the polar coordinate system
                    x cosΘ + y sinΘ = r

            Hough Transformation Algorithm
            -------------------------------

    1. Edge detection, e.g Using the Canny Edge
        Detector.
    2. Mapping of the edge points to the Hough 
        space and storage in an accumulator
    3. Interpretation of the accumulator to 
        yield lines of infinite length. The 
        interpretation is done by thresholding 
        and possibly other constraints.
    4. Conversion of infinite lines to finite lines.


        OpenCV's Two kinds of Hough line Transforms
        -------------------------------------------

        o The Standard Hough Transform (HoughLines method)
        o The Probabilistic Hough Line Transform (HoughLinesP)
    '''
    img = cv.imread("./img/sudoku.jpg")
    img = cv.resize(img, (500, 500))
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray_img, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        # x1 stores the rounded off value of (r* cosΘ - 1000 * sinΘ)
        x1 = int(x0 + 1000 * (-b))
        # y1 stores the rounded off value of (r * sinΘ + 1000 * cosΘ)
        y1 = int(y0 + 1000 * (a))
        # x2 stores the rounded off value of (r * cosΘ + 1000 * sinΘ)
        x2 = int(x0 - 1000 * (-b))
        # y2 stores the rounded off value of (r * sinΘ - 1000 * cosΘ)
        y2 = int(y0 - 1000 * (a))

        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv.imshow("Image", img)
    cv.imshow("Canny", edges)

    cv.waitKey()
    cv.destroyAllWindows()


def houghP():
    img = cv.imread("./img/road.jpg")
    img = cv.resize(img, (500, 500))
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray_img, 170, 200, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100,
                           minLineLength=100, maxLineGap=10)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv.imshow("Image", img)
    cv.imshow("Canny", edges)

    cv.waitKey()
    cv.destroyAllWindows()

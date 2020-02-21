import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def contours():
    '''
    CONTOURS is a python list of all the contours in the image.
    Each individual contour is a NumPy array of (x,y) coordinates
    of boundary points of the object.
    '''
    img = cv.imread("./img/rohit.jpg")
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Black Background
    black = np.zeros((img.shape[0], img.shape[1], 3))

    ret, thresh = cv.threshold(img_gray, 127, 255, 0)

    contours, hierarchy = cv.findContours(
        thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    print(f"Number of Countours = {len(contours)}")
    print(contours[0])

    cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    cv.drawContours(black, contours, -1, (0, 255, 0), 3)

    cv.imshow("Image", img)
    cv.imshow("Black", black)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    contours()

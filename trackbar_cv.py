import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def change(x):
    # print(x)
    pass


def trackbar():
    img = np.zeros((300, 512, 3), np.uint8)
    cv.namedWindow("image")

    cv.createTrackbar('B', 'image', 0, 255, change)
    cv.createTrackbar('G', 'image', 0, 255, change)
    cv.createTrackbar('R', 'image', 0, 255, change)

    switch = '0: OFF\n 1: ON'
    cv.createTrackbar(switch, 'image', 0, 1, change)

    while True:
        cv.imshow("image", img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

        b = cv.getTrackbarPos('B', 'image')
        g = cv.getTrackbarPos('G', 'image')
        r = cv.getTrackbarPos('R', 'image')
        s = cv.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv.destroyAllWindows()


if __name__ == '__main__':
    trackbar()

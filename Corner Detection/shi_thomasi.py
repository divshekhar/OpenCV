import cv2 as cv
import numpy as np


def shiThomasi():

    gray = cv.imread("./img/chess.jpg", 0)

    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    corners = cv.goodFeaturesToTrack(gray, 20, 0.01, 50)

    # corners = np.int0(corners)

    for i in corners:
        # x, y = i.ravel()
        x, y = i[0]
        x = int(x)
        y = int(y)
        cv.circle(gray, (x, y), 3, (0, 255, 0), -1)

    cv.imshow('dst', gray)

    cv.waitKey()
    cv.destroyAllWindows()


shiThomasi()

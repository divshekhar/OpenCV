import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def histogram():
    # img = np.zeros((500, 500), np.uint8)
    # cv.rectangle(img, (50, 50), (250, 250), (255), -1)
    # cv.rectangle(img, (250, 250), (450, 450), (127), -1)

    img = cv.imread("./img/sea.jpg")

    cv.imshow("Histogram", img)
    b, g, r = cv.split(img)
    plt.hist(b.ravel(), 256, [0, 256])
    plt.hist(g.ravel(), 256, [0, 256])
    plt.hist(r.ravel(), 256, [0, 256])
    plt.show()

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "main":
    histogram()

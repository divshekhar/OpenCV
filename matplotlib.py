import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def matplotlib():
    img = cv.imread("./img/balls.jpg")
    # OpenCV stores image in BGR format
    cv.imshow("Gradient", img)

    # Convert image from BGR to RGB
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # matplotlib stores image in RGB format
    plt.imshow(img)
    plt.show()

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    matplotlib()

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def translation():
    image = cv.imread('./img/sea.jpg')
    height, width = image.shape[:2]
    print(image.shape[:2])
    quater_height, quater_width = height/4, width/4
    T = np.float32([[1, 0, quater_width], [0, 1, quater_height]])
    img_translation = cv.warpAffine(image, T, (width, height))
    cv.imshow("Translation", img_translation)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main":
    translation()

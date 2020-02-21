import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# Template Matching


def temp_match():
    img = cv.imread("./img/rohitSharma.jpg")
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_img = cv.imread("./img/rohitSharmaFace.jpg", 0)  # Template
    w, h = face_img.shape[::-1]

    res = cv.matchTemplate(gray_image, face_img, cv.TM_CCOEFF_NORMED)
    # print(res)

    threshold = 0.99

    loc = np.where(res >= threshold)
    print(loc)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 2)
    cv.imshow("Original Image", img)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    temp_match()

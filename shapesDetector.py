import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def shapes():
    img = cv.imread('./img/shapess.jpg')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    _, thresh = cv.threshold(img_gray, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    white = np.ones((img.shape[0], img.shape[1], 3))

    for c in contours:
        approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
        cv.drawContours(img, [approx], 0, (0, 255, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            cv.putText(img, "Triangle", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        elif len(approx) == 4:
            x1, y1, w, h = cv.boundingRect(approx)
            aspect_ratio = float(w) / float(h)
            print(aspect_ratio)
            if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                cv.putText(img, "Square", (x, y),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
            else:
                cv.putText(img, "Rectangle", (x, y),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        elif len(approx) == 5:
            cv.putText(img, "Pentagon", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        elif len(approx) == 10:
            cv.putText(img, "Star", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        else:
            cv.putText(img, "Circle", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

    cv.imshow("Shapes", img)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    shapes()

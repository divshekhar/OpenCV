import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def drawShapes():
    image = cv.imread('./img/sea.jpg')
    # img = np.zeros([600, 800, 3], np.uint8)
    # line
    image = cv.line(image, (40, 100), (255, 255), (0, 0, 255), 5)
    # Arrowed Line
    image = cv.arrowedLine(image, (0, 255), (500, 350), (0, 0, 255), 5)
    # Rectangle
    image = cv.rectangle(image, (400, 250), (750, 400), (0, 0, 255), 5)
    # Circle
    image = cv.circle(image, (550, 350), 150, (0, 0, 255), 5)
    # Text
    font = cv.FONT_HERSHEY_COMPLEX
    image = cv.putText(image, "OpenCV", (10, 500), font,
                       4, (0, 255, 0), 10, cv.LINE_AA)
    # show image
    cv.imshow('Shapes', image)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    drawShapes()

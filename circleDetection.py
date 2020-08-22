import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def circleDetection():
    '''
    (x-xc)^2 + (y-yc)^2 = r^2   
    #Formula of circle
    '''
    img = cv.imread('./img/coins.jpg')
    img = cv.resize(img, (700, 400))
    output = img.copy()
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(gray_img, 5)
    circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT,
                              1, 100, 10, param1=130, param2=55, minRadius=5, maxRadius=0)
    # circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT,
    #                           1, 10)
    detected_circles = np.uint16(np.around(circles))

    for (x, y, r) in detected_circles[0, :]:
        cv.circle(output, (x, y), r, (0, 255, 0), 3)
        cv.circle(output, (x, y), 2, (255, 0, 0), 3)

    cv.imshow("Original Image", img)
    cv.imshow("Output", output)
    cv.waitKey()
    cv.destroyAllWindows()


circleDetection()

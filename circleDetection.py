import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt


def circleDetection():
    '''
    (x-xc)^2 + (y-yc)^2 = r^2   
    #Formula of circle
    '''
    img = cv.imread('./img/balls2.jpg')
    img = cv.resize(img, (500, 400))
    output = img.copy()
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(gray_img, 5)
    circles = cv.HoughCircles(gray_img, cv.HOUGH_GRADIENT,
                              1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

    detected_circles = np.uint16(np.around(circles))

    for (x, y, r) in detected_circles[0, :]:
        cv.circle(output, (x, y), r, (0, 255, 0), 3)
        cv.circle(output, (x, y), 2, (255, 0, 0), 3)

    cv.imshow("Original Image", img)
    cv.imshow("Output", output)
    cv.waitKey()
    cv.destroyAllWindows()


circleDetection()

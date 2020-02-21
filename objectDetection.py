import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def change(x):
    # print(x)
    pass


def objectDetection():
    cv.namedWindow("Tracking")
    cv.createTrackbar("LH", "Tracking", 0, 255, change)
    cv.createTrackbar("LS", "Tracking", 0, 255, change)
    cv.createTrackbar("LV", "Tracking", 0, 255, change)
    cv.createTrackbar("UH", "Tracking", 255, 255, change)
    cv.createTrackbar("US", "Tracking", 255, 255, change)
    cv.createTrackbar("UV", "Tracking", 255, 255, change)
    img = cv.imread('./img/balls.jpg')
    #  for Video capture and object detection
    # cap = cv.VideoCapture(0)
    while True:
        # _, img = cap.read()
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        l_h = cv.getTrackbarPos("LH", "Tracking")
        l_s = cv.getTrackbarPos("LS", "Tracking")
        l_v = cv.getTrackbarPos("LV", "Tracking")

        u_h = cv.getTrackbarPos("UH", "Tracking")
        u_s = cv.getTrackbarPos("US", "Tracking")
        u_v = cv.getTrackbarPos("UV", "Tracking")

        l_c = np.array([l_h, l_s, l_v])
        u_c = np.array([u_h, u_s, u_v])

        # print(l_c)
        # print(u_c)

        # u_b = np.array([130, 255, 255])
        # l_b = np.array([110, 50, 50])

        mask = cv.inRange(hsv, l_c, u_c)
        res = cv.bitwise_and(img, img, mask=mask)

        cv.imshow("Object Detection", res)
        cv.imshow("mask", mask)
        cv.imshow("Original Image", img)

        k = cv.waitKey(1) & 0xFF
        if k == 27:
            print(l_c)
            print(u_c)
            break
    # cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    objectDetection()

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def captureVideo():

    cap = cv.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow('frame', gray_frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    captureVideo()

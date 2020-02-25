import numpy as np
import cv2 as cv


def bs():
    cap = cv.VideoCapture('./img/vtest.avi')

    # fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False)
    fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)

    while cap.isOpened():
        ret, frame = cap.read()

        if frame is None:
            break

        fgmask = fgbg.apply(frame)

        cv.imshow('Frame', frame)
        cv.imshow('FG Mask', fgmask)
        if cv.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


bs()

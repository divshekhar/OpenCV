import cv2 as cv
import numpy as np


def meanShift():
    cap = cv.VideoCapture('./img/slow_traffic_small.mp4')
    # take first frame of the video
    ret, frame = cap.read()
    # setup initial location of window
    x, y, width, height = 300, 200, 100, 50
    track_window = (x, y, width, height)
    # set up the ROI for tracking
    roi = frame[y:y+height, x:x+width]
    hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
                      np.array((180., 255., 255)))
    roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
    # Setup the termination criteria, either 10 iterations or move by atleast 1 pt
    term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
    while True:
        ret, frame = cap.read()

        if ret:

            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
            # Apply meanshift to get the new location.
            ret, track_window = cv.meanShift(dst, track_window, term_crit)
            #  Draw it on the image
            x, y, w, h = track_window
            final_image = cv.rectangle(
                frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv.imshow("Frame", final_image)
            k = cv.waitKey(30) & 0xFF
            if k == ord('q'):
                break
        else:
            break
    cap.release()
    cv.destroyAllWindows()


meanShift()

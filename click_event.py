import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def click_event(event, x, y, flags, params):
    '''
    Left Click to get the x, y coordinates.
    Right Click to get BGR color scheme at that position.
    '''
    text = ''
    font = cv.FONT_HERSHEY_COMPLEX
    color = (255, 0, 0)
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ",", y)
        text = str(x) + "," + str(y)
        color = (0, 255, 0)
    elif event == cv.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        text = str(b) + ',' + str(g) + ',' + str(r)
        color = (0, 0, 255)
    cv.putText(img, text, (x, y), font, 0.5, color, 1, cv.LINE_AA)
    cv.imshow('image', img)


# img = np.zeros((600, 600, 3), np.uint8)
img = cv.imread('./img/sea.jpg')
print(img)
cv.imshow('image', img)
cv.setMouseCallback('image', click_event)
cv.waitKey()
cv.destroyAllWindows()

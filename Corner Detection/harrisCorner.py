import cv2 as cv
import numpy as np


def harrisCorner():
    '''
            Harris Corner Detector
            ----------------------
    1.) Determine which windows produce very large
        variations in intensity when moved in both 
        X and Y directions.
    2.) With each such window found, a score R is
        computed.
    3.) After applying a threshold to this score,
        important corners are selected & marked.
    '''
    img = cv.imread("./img/chess.jpg")

    # cv.imshow("Original Image", img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # cornerHarris takes gray image in form of float32
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 3, 3, 0.04)
    '''
            Parameters
            ----------
    1.) img - Input image, it should be grayScale
                and float32 type.
    2.) blockSize - It is the size of neighbourhood
                    considered for corner detection.
    3.) ksize - Aperture parameter of Sobel derivative
                used.
    4.) k - Harris detector free parameter in the 
            equation.
    '''

    dst = cv.dilate(dst, None)

    img[dst > 0.01 * dst.max()] = [0, 255, 0]

    cv.imshow("dst", img)
    cv.waitKey()
    cv.destroyAllWindows()


harrisCorner()

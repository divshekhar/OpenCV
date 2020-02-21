import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def blend():
    '''
    Image Blending Using Pyramid
    1. Load two images
    2. Find Gaussian Pyramids for two images. Upto 6 level
    3. From Gaussian Pyramids,find their Laplacian Pyramids.
    4. Now Join the images in each levels of laplacian P.
    5. Finally from this joint image Pyramids, reconstruct the
        Original Image.
    '''
    n1 = cv.imread("./img/nature1.jpg")
    n2 = cv.imread("./img/nature2.jpg")

    print(n1.shape)
    print(n2.shape)

    # n1_n2 = np.hstack((n1[:, :256], n2[:, 256:]))

    '''
    Generate Gaussian Pyramid for Nature 1
    '''
    n1_copy = n1.copy()
    gp_n1 = [n1_copy]

    for i in range(6):
        n1_copy = cv.pyrDown(n1_copy)
        gp_n1.append(n1_copy)

    '''
    Generate Gaussian Pyramid for Nature 2
    '''
    n2_copy = n2.copy()
    gp_n2 = [n2_copy]

    for i in range(6):
        n2_copy = cv.pyrDown(n2_copy)
        gp_n2.append(n2_copy)

    '''
    Laplacian Pyramid for Nature 1
    '''
    n1_copy = gp_n1[5]
    lp_n1 = [n1_copy]

    for i in range(5, 0, -1):
        gp_ex = cv.pyrUp(gp_n1[i])
        lap = cv.subtract(gp_n1[i-1], gp_ex)
        lp_n1.append(lap)

    '''
    Laplacian Pyramid for Nature 2
    '''
    n2_copy = gp_n2[5]
    lp_n2 = [n2_copy]

    for i in range(5, 0, -1):
        gp_ex = cv.pyrUp(gp_n2[i])
        lap = cv.subtract(gp_n2[i-1], gp_ex)
        lp_n2.append(lap)

    '''
    Join Half the Pyramid
    '''
    n1_n2_pyramid = []
    n = 0
    for n1_lap, n2_lap in zip(lp_n1, lp_n2):
        n += 1
        cols, rows, ch = n1_lap.shape
        laplacian = np.hstack(
            (n1_lap[:, 0:int(cols/2)], n2_lap[:, int(cols/2):]))
        n1_n2_pyramid.append(laplacian)

    '''
    Reconstruct
    '''
    reconstruct = n1_n2_pyramid[0]
    for i in range(1, 6):
        reconstruct = cv.pyrUp(reconstruct)
        reconstruct = cv.add(n1_n2_pyramid[i], reconstruct)

    # cv.imshow("Nature 1", n1)
    # cv.imshow("Nature 2", n2)
    cv.imshow("N1_N2", reconstruct)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    blend()

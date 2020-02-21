import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def morphologicalTransformation():
    img = cv.imread('./img/balls2.jpg', 0)
    _, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

    kernel = np.ones((5, 5), np.uint8)

    dilation = cv.dilate(mask, kernel, iterations=2)
    erosion = cv.erode(mask, kernel, iterations=1)
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
    th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

    titles = ["Original Image", "Mask", "Dilation",
              "Erosion", "Opening", "Closing", "mg", "th"]
    images = [img, mask, dilation, erosion, opening, closing, mg, th]

    for i in range(len(images)):
        plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == '__main__':
    morphologicalTransformation()

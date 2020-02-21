import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# Gradients

def gradient():
    img = cv.imread("./img/rohit.jpg", 0)
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
    lap = np.uint8(np.absolute(lap))

    sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
    sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

    sobleX = np.uint8(np.absolute(sobelX))
    sobleY = np.uint8(np.absolute(sobelY))

    sobelCombined = cv.bitwise_or(sobelX, sobelY)

    title = ["Original Image", "Laplacian",
             "SobelX", "SobelY", "Combined Sobel(or)"]
    images = [img, lap, sobleX, sobelY, sobelCombined]

    for i in range(len(images)):
        plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
        plt.title(title[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == "__main__":
    gradient()

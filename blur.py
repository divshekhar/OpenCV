import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def blurring():
    # img = cv.imread('./img/salt.png')
    img = cv.imread('./img/rohit.jpg')

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    kernel = np.ones((5, 5), np.float32)/25
    dst = cv.filter2D(img, -1, kernel)
    blur = cv.blur(img, (5, 5))
    gblur = cv.GaussianBlur(img, (5, 5), 0)
    median = cv.medianBlur(img, 5)
    bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)

    titles = ["Original Image", "2D Convolution", "Blur",
              "GaussianBlur", "Median", "Bilateral Filter"]
    images = [img, dst, blur, gblur, median, bilateralFilter]

    for i in range(len(images)):
        plt.subplot(2, 3, i+1), plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == '__main__':
    blurring()

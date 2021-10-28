import numpy as np
import pandas as pd
import cv2 as cv 
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt

# The list to store all images
urls = ["https://images.ctfassets.net/hrltx12pl8hq/3MbF54EhWUhsXunc5Keueb/60774fbbff86e6bf6776f1e17a8016b4/04-nature_721703848.jpg?fit=fill&w=480&h=270"]  
# print all images in list
for url in urls:
  image = io.imread(url) 
  image2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  final = cv.hconcat((image, image2))
  cv2_imshow(final)
  print('\n')
  
#Transforming to greyscale image 
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv2_imshow(gray_image)

# For brighter effect
image3 = (100.0/255)*gray_image + 100
cv2_imshow(image3)

# For darker effect with less brightness
image4 = 255.0*(gray_image/255.0)**2
cv2_imshow(image4)

#Performing histogram equalization
def histeq(im, nbr_bins = 256):
  """ Histogram equalization  """
  # get the image histogram
  imhist, bins = np.histogram(im.flatten(), nbr_bins, [0, 256])
  cdf = imhist.cumsum() 
  #normalization of the image
  cdf = imhist.max()*cdf/cdf.max() 
  cdf_mask = np.ma.masked_equal(cdf, 0)
  cdf_mask = (cdf_mask - cdf_mask.min())*255/(cdf_mask.max()-cdf_mask.min())
  cdf = np.ma.filled(cdf_mask,0).astype('uint8')
  return cdf[im.astype('uint8')]

# print the final image
image5 = histeq(image4)
cv2_imshow(image5)

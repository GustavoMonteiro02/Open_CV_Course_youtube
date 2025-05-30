#pylint:disable=no-member
# most of the operations made here can be done contaraly except for grayscale

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (hue saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)


#OpenCV reads images as BGR unlike most other libraries using RGB
# plt.imshow(img)
# plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)
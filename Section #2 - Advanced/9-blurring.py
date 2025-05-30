#pylint:disable=no-member
#smoothing and bluring in opencv
#we smooth an image when there is a not of noise (camera senses, lightnings, etc...)
# kernel is the windows selected on the image to blur
# kernel size is the number of rows and columns on the window
# the pixels are blured in relation with its surrounding pixels

import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging, will compute the pixel intensity of the middle pixes of the kernel as the average of the surrounding pixel intensities
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# # Gaussian Blur, same as average but instead of computing thr average of the surrounding pixel intensities it sets a weight on each of those pixels (gets less blur but more natural)
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# # Median Blur, same as averaging instead of average of teh surrounding pixels its finds the medium (generrally more effective to reduce noise than gaussian and average), genrally not meant for hight kernel sizes
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#  Bilateral, most effective by carefully checking for blurred edges and maintaining them
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
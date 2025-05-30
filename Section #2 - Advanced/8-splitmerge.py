#pylint:disable=no-member
# A colored image is made of multiple color channels Red, Green and Blue 

import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# they will be represented as grayscale where lighter parts show more intense presence of that pixel color and darker shows less/none
b,g,r = cv.split(img)
cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)

# if instead of grayscale we cans the the actual color involved (seing the distribution much better) by using the BGR color channels correctly
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape) #(427, 640, 3) size and 3 color shannels
print(b.shape) # (427, 640) size only (1 color channel)
print(g.shape) # (427, 640) size only (1 color channel)
print(r.shape) # (427, 640) size only (1 color channel)

# by merging the color channels the original image is returned
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
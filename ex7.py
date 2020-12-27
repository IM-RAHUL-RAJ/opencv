# find contours

from cv2 import cv2
import numpy as np

originalImage =cv2.imread('E:/opencv-for-github/cards2.jpg')

cv2.imshow('img',originalImage)
#convert into gray scale

grayimg=cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)
#convert into edges

canny=cv2.Canny(grayimg,40,250)

cv2.imshow('img',canny)
cv2.waitKey(0)

# make a copy of the canny image since contours alters image

cannyCopy=canny.copy()

#identify contours in images
contours,hierarchy=cv2.findContours(cannyCopy,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#drawng contours and
cv2.drawContours(originalImage,contours,-1,(255,0,0),3)

cv2.imshow('Contours',originalImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
from cv2 import cv2
import numpy as np
# //horizontally stacking two images
img=cv2.imread('E:/opencv-for-github/cards2.jpg')

hor=np.hstack((img,img,img))
# //vertically stacking two images

ver=np.vstack((img,img))

cv2.imshow("name",hor)
cv2.waitKey(0)
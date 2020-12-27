from cv2 import cv2
import numpy as np

img=cv2.imread('E:/opencv-for-github/cards2.jpg')

# cv2.imshow('cards2',img)
# cv2.waitKey(0)

width, height=400,400
pt1=np.float32([[111,219],[400,100],[154,482],[352,440]])
pt2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pt1,pt2)
imgOut=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('image',imgOut)
cv2.waitKey(0)
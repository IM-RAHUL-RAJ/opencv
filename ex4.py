# MAKING SHAPES

from cv2 import cv2

import numpy as np

img=np.zeros((512,512,3),np.uint8)
# img[200:300,100:300]=255,0,0  adding color

# adding a line/////
cv2.line(img,(0,0),(200,200),(0,0,255),3)  
cv2.rectangle(img,(0,0),(250,250),(0,0,255),6)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1.2,(150,0,20),2)
cv2.imshow('image',img)
cv2.waitKey(0)
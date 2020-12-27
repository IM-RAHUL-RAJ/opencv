import numpy as np
from cv2 import cv2

classifyImage=cv2.CascadeClassifier('C:/Python38/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
originalImage=cv2.imread('E:/opencv-for-github/face2.jpeg')
grayImg=cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)

# region of interest tro detect the face
faceROI=classifyImage.detectMultiScale(grayImg,2,1)

# check if face ROI tuple is empty or not

if faceROI is ():
    print('No face detected')

#iterate through face data and draw2a rectangle around

for(x,y,w,h) in faceROI:
    cv2.rectangle(originalImage,(x,y),(x+w,y+h),(127,0,250),2)
    cv2.imshow('face detect resut',originalImage)
    cv2.waitKey(0)

cv2.destroyAllWindows()    
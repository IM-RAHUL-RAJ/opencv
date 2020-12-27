from cv2 import cv2

img=cv2.imread('E:/opencv-for-github/low-image-quality.jpg')
# cv2.imshow('rahul',img)
# cv2.waitKey(0)
# //grayscale image
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# /////blurr image 
imgblur=cv2.GaussianBlur(img,(7,7),0)

imgCanny=cv2.Canny(img,100,100)

cv2.imshow('gray',imgCanny)
cv2.waitKey(0)
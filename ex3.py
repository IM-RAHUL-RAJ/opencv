from cv2 import cv2

img=cv2.imread('E:/opencv-for-github/low-image-quality.jpg')

print(img.shape)

imgResize=cv2.resize(img,(300,200))
print(imgResize.shape)
# cv2.imshow('size',imgResize)
# cv2.waitKey(0)

# crop image//////////
imgcrop=img[0:200,200:500]
cv2.imshow('crop',imgcrop)
cv2.waitKey(0)

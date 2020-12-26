from cv2 import cv2
# """uploading a pic""////////////////////////////////////////////////////////////
# img=cv2.imread('E:/opencv-for-github/low-image-quality.jpg')
# print(img) 

# cv2.imshow('rahul',img)
# cv2.waitKey(0)

# """uploading a video""////////////////////////////////////////////////////////////


# cap=cv2.VideoCapture('D:/Bandicam/newvideo.mp4')
# while True:
#     success,image=cap.read()
#     cv2.imshow('video',image)
#     if(cv2.waitKey(100)==13):
#         break
# """videocapuring""webcam///////////////////////


cap2=cv2.VideoCapture(0)
cap2.set(3,640)
cap2.set(4,480) 
while True:
  ret,frame=cap2.read()
  cv2.imshow("raj",frame)
  if cv2.waitKey(3000)==13:
    break
# cap2.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('C:/py_vision/hong.jpg')

#res = cv2.resize(img,None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 1*height), interpolation = cv2.INTER_CUBIC) # Manual Size지정
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) #이미지축소
zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # 배수 Size지정
# zoom3 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
# zoom4 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

#보간법 interpolation
#INTER_NEAREST: a nearest-neighbor interpolation;
#INTER_LINEAR: a bilinear interpolation;
#INTER_AREA: resampling using pixel area relation;
#INTER_CUBIC: a bicubic interpolation over 4x4 pixel neighborhood;


# cv2.imshow('img', img)
# cv2.imshow('res', res)
cv2.imshow('zoom2', zoom2)
cv2.imshow('zoom3', zoom3)
cv2.imshow('zoom4', zoom4)

cv2.waitKey(0)
cv2.destroyAllWindows()

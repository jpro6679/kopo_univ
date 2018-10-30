# #Filename : contour.py
# import numpy as np
# import cv2
#
# img = np.zeros((300,400, 3), np.uint8)
# img_1 = np.zeros((300,400, 3), np.uint8)
#
# rec = cv2.rectangle(img,(50,100),(350,200),(255,255,255),-1)
#
# img = rec.copy()
# img_1 = rec.copy()
#
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgray1 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
#
# ret,thresh = cv2.threshold(imgray,200,255, cv2.THRESH_BINARY_INV)
# _,thresh1 = cv2.threshold(imgray1,200,255, cv2.THRESH_BINARY_INV)
#
# # 이미지에서 contour를 탐색한다
# image1, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE) #cv2.CHAIN_APPROX_NONE #cv2.CHAIN_APPROX_SIMPLE
# _, contours1, _ = cv2.findContours(thresh1,cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE) #cv2.CHAIN_APPROX_NONE #cv2.CHAIN_APPROX_SIMPLE
#
# print("contours:",contours)
# print("contours1:",contours1)
#
# print(len(contours))
# print(len(contours1))
#
# # 탐색된 contour를 원본 이미지에 그린다
# cv2.drawContours(img, contours, 1, (0,0,255), 1) #3번째 인덱스 변경, -1은 전체인덱스
# cv2.drawContours(img_1, contours1, 1, (0,0,255), 1) #3번째 인덱스 변경, -1은 전체인덱스
#
#
# cv2.imshow('img', img)
# cv2.imshow('img_1', img_1)
# # cv2.imshow('gray', imgray)
# # cv2.imshow('threshold', thresh)
# # cv2.imshow('contour', image1)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Filename : approx.py
import numpy as np
import cv2

# 400 x 300의 칼라 영역을 생성한다
img = np.zeros((300,400, 3), np.uint8)

# White 칼라의 직사각형을 그린다.
img1 = cv2.rectangle(img,(50,100),(350,200),(255,255,255),-1)
# 사각형을 복사한다.
img2 = img1.copy()
# 이미지를 그레이스케일로 변환한다.
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# CHAIN_APPROX_NONE 근사법으로 Contour를 찾는다.
image1, contours1, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# CHAIN_APPROX_SIMPLE 근사법으로 Contour를 찾는다.
image2, contours2, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print('APPROX_NONE : ', contours1[0].shape)
print('APPROX_SIMPLE : ', contours2[0].shape)
print(contours1)
print(contours2)

# 이미지에 Contour를 그린다.
for i in contours1[0]:
    cv2.circle(img1, (i[0][0], i[0][1]), 3, (0, 0, 255), -1)

for i in contours2[0]:
    cv2.circle(img2, (i[0][0], i[0][1]), 3, (0, 0, 255), -1)

cv2.imshow('APPROX_NONE', img1)
cv2.imshow('APPROX_SIMPLE', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


#Filename : moment.py

import cv2
import numpy as np

img = cv2.imread('star.jpg')
img1 = img.copy()
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 120,255,0)

image, contours, hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


#첫 번째 contour에 대한 모멘트 정보를 출력한다.
mom = contours[0]
M = cv2.moments(mom)

print(M)
#중심구하기##########################################
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print('cx : ', cx)
print('cy : ', cy)
img = cv2.circle(img1, (385, 389), 10, (0, 0, 255), -1)
###########################################################

#면적구하기########################
area = cv2.contourArea(mom)
print(area, M['m00'])
##################################################

#둘레구하기###################################
perimeter = cv2.arcLength(mom, False)
print(perimeter)
perimeter = cv2.arcLength(mom, True)
print(perimeter)
############################################

cv2.drawContours(img, contours, -1, (0,0,255), 5) #3번째 인덱스 변경, -1은 전체인덱스

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


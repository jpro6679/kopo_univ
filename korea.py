import cv2
import numpy as np

img = cv2.imread('korea.jpg')
img1 = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_ , img_bin = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

_ , contours, _ = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

momentom_1 = contours[0]
momentom_2 = contours[1]
momentom_3 = contours[2]
momentom_4 = contours[3]

# momentom_1_inform = cv2.moments(momentom_1)
# momentom_2_inform = cv2.moments(momentom_1)
# momentom_3_inform = cv2.moments(momentom_1)
# momentom_4_inform = cv2.moments(momentom_1)

momentom_1_area = cv2.contourArea(momentom_1)
momentom_2_area = cv2.contourArea(momentom_2)
momentom_3_area = cv2.contourArea(momentom_3)
momentom_4_area = cv2.contourArea(momentom_4)

momentom_max = [momentom_1_area, momentom_2_area, momentom_3_area, momentom_4_area]
momentom_max.sort(reverse=True)

if momentom_max[0] == momentom_1_area:
    i = 0
elif momentom_max[0] == momentom_2_area:
    i = 1
elif momentom_max[0] == momentom_3_area:
    i = 2
elif momentom_max[0] == momentom_4_area:
    i = 3

cnt = contours[i]
cvx_hull = cv2.convexHull(cnt)

cv2.drawContours(img, [cvx_hull], -1, (0,255,0), 3)
cv2.drawContours(img1, [cvx_hull], 0, (0,255,0), 3)



cv2.imshow('img',img)
cv2.imshow('img1',img1)
cv2.waitKey(0)
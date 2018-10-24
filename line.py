# import numpy as np
# import cv2
#
# img = np.zeros((512,512,3), np.uint8) #캔버스(도화지)만들기
#
# # cv2.line(image, (top, left), (bottom, right), (B, G, R), thickness)
# img = cv2.line(img,(0,0),(511,551),(255,0,0),5)
# img = cv2.line(img,(551,551),(0,0),(0,255,0),5)
# img = cv2.line(img,(0,551),(551,0),(0,0,255),5)
# img = cv2.line(img,(551,0),(551,0),(0,0,255),5)
#
# cv2.imshow('image', img)
#
# cv2.waitKey(0)
#################################################################################
# import numpy as np
# import cv2
#
# img = np.zeros((512,512,3), np.uint8)
#
# #cv2.Rectangle(image, (top, left), (bottom, right), (B, G, R), thickness)
#
# img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) #thickness를 -1로 두면 색이 채워짐
#
# cv2.imshow('image', img)
# cv2.waitKey(0)
##################################################################################
# import numpy as np
# import cv2
#
# img = np.zeros((512,512,3), np.uint8)
#
# #cv2.Circle (image, (x, y), radius, (B, G, R), thickness)
#
# img = cv2.circle(img,(255,255), 255, (0,0,255), 10)
# img = cv2.circle(img,(255,255), 170, (0,255,0), 10)
# img = cv2.circle(img,(255,255), 85, (255,0,0), 10)
#
# cv2.imshow('image', img)
# cv2.waitKey(0)
##################################################################################
import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

#cv2.ellipse(image, (x, y), axes, angle, startAngle, endAngle, (B, G, R), thickness)

img = cv2.ellipse(img,(256,256),(100,100),0,90,0,255,-1)

cv2.imshow('image', img)
cv2.waitKey(0)
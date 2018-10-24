import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #만약 hsv색상을 모른다면? ->내가원하는 rgb색을 조립해서 hsv로 변환시켜서 프린트시켜보면됨.
    # red = np.uint8([[[0,0,255]]])
    # hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    # hsv_red


    # define range of blue color in HSV
    lower_red = np.array([0,74,79])
    upper_red = np.array([0,255,255])
    lower_color2 = np.array([110,50,50])
    upper_color2 = np.array([150,255,255])
    lower_color3 = np.array([0, 0, 0])
    upper_color3 = np.array([80, 80, 80])


    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_color2, upper_color2)
    mask3 = cv2.inRange(hsv, lower_color3, upper_color3)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask2)
    res3 = cv2.bitwise_and(frame, frame, mask=mask3)


    cv2.imshow('res',res)
    cv2.imshow('res2',res2)
    cv2.imshow('res3',res3)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

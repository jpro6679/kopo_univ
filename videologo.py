import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([150,255,255])

    lower_green = np.array([40,50,50])
    upper_green = np.array([80,255,255])

    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask1 = cv2.inRange(hsv, lower_green, upper_green)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res1 = cv2.bitwise_and(frame,frame, mask= mask1)
    res2 = cv2.bitwise_and(frame,frame, mask= mask2)

    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('res1',res1)
    cv2.imshow('res2',res2)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

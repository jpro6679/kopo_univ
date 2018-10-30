import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


img = cv2.imread('all.jpg', 0)
img2 = cv2.imread('all.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

cv2.namedWindow('edge')
cv2.createTrackbar('Min', 'edge', 0, 255, nothing)
cv2.createTrackbar('Max', 'edge', 0, 255, nothing)

while (True):
    max = cv2.getTrackbarPos('Max', 'edge')
    min = cv2.getTrackbarPos('Min', 'edge')
    edges = cv2.Canny(dst, min, max)
    cv2.imshow('img', img)
    cv2.imshow('dst', dst)
    cv2.imshow('edge', edges)


    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

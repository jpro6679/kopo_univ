import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('capture.jpg')

kernel = np.ones((3,3),np.float32)/9
dst = cv2.filter2D(img,-1,kernel)

kernel2 = np.ones((5,5),np.float32)/25
dst2 = cv2.filter2D(img,-1,kernel2)

kernel3 = np.ones((7,7),np.float32)/49
dst3 = cv2.filter2D(img,-1,kernel3)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)

cv2.waitKey(0)

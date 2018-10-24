import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/py_vision/jim_sniper2.jpg')

kernel = np.ones((5,5),np.float32)/4
dst1 = cv2.filter2D(img,-1,kernel)

kernel2 = np.ones((5,5),np.float32)/36
dst2 = cv2.filter2D(img,-1,kernel2)

kernel3 = np.ones((5,5),np.float32)/25
dst3 = cv2.filter2D(img,-1,kernel3)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey(0)

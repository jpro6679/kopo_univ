import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo.jpg')

blur = cv2.blur(img,(3,3))
blur2 = cv2.blur(img,(5,5))
blur3 = cv2.blur(img,(7,7))

cv2.imshow('img',img)
cv2.imshow('blur',blur)
cv2.imshow('blur2',blur2)
cv2.imshow('blur3',blur3)

cv2.waitKey(0)
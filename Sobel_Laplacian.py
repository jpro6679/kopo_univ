import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('flippygray.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx2 = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelx3 = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=7)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely2 = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobely3 = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=7)

j = sobelx + sobely
j2 = sobelx2 + sobely2
j3 = sobelx3 + sobely3

cv2.imshow('img',img)
cv2.imshow('laplacian',laplacian)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobelx2',sobelx2)
cv2.imshow('sobelx3',sobelx3)
cv2.imshow('sobely',sobely)
cv2.imshow('sobely2',sobely2)
cv2.imshow('sobely3',sobely3)
cv2.imshow('j',j)
cv2.imshow('j2',j2)
cv2.imshow('j3',j3)

cv2.waitKey(0)
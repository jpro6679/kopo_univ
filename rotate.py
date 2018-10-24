import cv2
import numpy as np

img = cv2.imread('cho.png',0)
rows,cols = img.shape

scale = 1
angle = 0

while(True):
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,scale)
    dst = cv2.warpAffine(img,M,(cols,rows))

    angle = angle + 10
    if angle == 360:
        angle = 0

    scale = scale - 0.01
    if scale < 0:
        break
    
    cv2.imshow('img',dst)
    if cv2.waitKey(50) == 27:
        break
    
cv2.destroyAllWindows()

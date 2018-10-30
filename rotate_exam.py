import cv2
import numpy as np
import math

img = cv2.imread('flippy.jpg',0)
rows, cols = img.shape

angle = 0

while True:
    print("angle:",angle)
    x = (cols / 2) * math.cos(angle * math.pi / 180) + (rows / 2) * math.sin(angle * math.pi / 180) # math.pi / 180 = 1도값
    print("x cos:",math.cos(angle * math.pi / 180))
    print("x sin:",math.sin(angle * math.pi / 180))
    y = (cols / 2) * math.sin(angle * math.pi / 180) - (rows / 2) * math.cos(angle * math.pi / 180)
    print("y cos:", math.cos(angle * math.pi / 180))
    print("y sin:", math.sin(angle * math.pi / 180))
    x = abs(x)
    y = abs(y)
    print("x",x)
    print("y",y)

    if x >= cols / 2:
        col = cols + int(x - cols / 2) * 2
    else:
        col = cols + int(y - cols / 2) * 2

    if y >= rows / 2:
        row = rows + int(y - rows / 2) * 2
    else:
        row = rows + int(x - rows / 2) * 2

    M = np.float32([[1, 0, abs(col - cols) / 2], [0, 1, abs(row - rows) / 2]])
    dst = cv2.warpAffine(img, M, (col, row))

    M = cv2.getRotationMatrix2D((col / 2, row / 2), angle, 1)
    dst = cv2.warpAffine(dst, M, (col, row))

    angle = angle + 1
    if angle == 360:
        angle = 0

    cv2.imshow('img', dst)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()

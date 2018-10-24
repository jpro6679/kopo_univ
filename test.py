import cv2
import numpy as np

img = cv2.imread('C:/py_vision/jim_sniper2.jpg', 0) # 이미지를 img변수에 입력한다.
rows,cols = img.shape # 이미지의 행과, 열을 rows와 cols에 넣는다.
angle = 0
scale = 1
while True:
    scale = scale - 0.01
    angle = angle + 10
    print(scale)
    if scale == -0.9900000000000014:
        scale = 1

    # M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    # 정답은 shrink빼고
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,scale)
    # angle과 scale을 더하고 빼줌
    dst = cv2.warpAffine(img, M, (cols,rows)) # translation된 dst변수
    # shrink = cv2.resize(dst, None, fx=x_size, fy=y_size, interpolation=cv2.INTER_AREA)  # 이미지축소


    cv2.imshow('dst',dst)
    # cv2.waitKey(100)

    k = cv2.waitKey(100) & 0xFF
    # if x_size is 0:
    #     break


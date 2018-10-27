import cv2
import numpy as np
from matplotlib import pyplot as plt

#이미지 불러오기
img = cv2.imread('C:/Users/jhm/Desktop/kopo_univ/all.JPG')
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rows, cols, _ = img.shape
print("rows:",rows), print("cols:",cols)
# #관심영역 자르기
# roi = img_rgb[0:rows, 0:cols]
#회색 변환
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#이미지 이진화로 저항의 몸체만 추출
_, img_bin = cv2.threshold(img_gray,240,255,cv2.THRESH_BINARY_INV)

i=0
j=0
my_xy = []
#왼쪽상단 꼭지점 구하기
print("hi",img_bin[530][273])
##################
for r in range(rows):
    for c in range(cols):
        if img_bin[r][c] == 255:
            left_top_x = c
            left_top_y = r
            print("bye", left_top_x, left_top_y)
            my_xy.append([left_top_x,left_top_y])
            print("zzz",my_xy[0])



#########################
# #오른쪽상단 꼭지점 구하기
# for i in range(cols):
#     for j in range(rows):
#         if img_bin[i][273-j] is 255:
#             right_top = 273-j
#             print(right_top)
#             break

# #저항 몸체 라벨링
# _, contours, _ = cv2.findContours(img_bin,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img_rgb, contours, -1, (0,255,0), 5)


#사각형 그리기
#cv2.Rectangle(image, (top, left), (bottom, right), (B, G, R), thickness)
# img_mask = cv2.rectangle(img_bin,(384,0),(510,128),(0,255,0),3)
plt.subplot(1,2,1), plt.imshow(img_rgb), plt.title('img_rgb')
plt.subplot(1,2,2), plt.imshow(img_bin), plt.title('img_bin')
plt.show()



#결과 확인
# cv2.imshow('img_bin',img_bin)






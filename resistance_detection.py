import cv2
import numpy as np
from matplotlib import pyplot as plt

#이미지 불러오기#############################################################
img = cv2.imread('C:/Users/jhm/Desktop/kopo_univ/4_7K.png')
rows, cols, _ = img.shape
print("rows:",rows), print("cols:",cols) #rows:행 531개 , cols:열 274개

#회색 변환##################################################################
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#이미지 이진화로 저항의 몸체만 추출#############################################
_, img_bin = cv2.threshold(img_gray,240,255,cv2.THRESH_BINARY_INV)

#저항몸체 라벨링하기##############################################################
    #상&하단값 구하기(=resistance_width)#########################################
width_xy = []
for i in range(rows):
    for j in range(cols):
        if img_bin[i][j] == 255:
            pixel_x = j
            pixel_y = i
            width_xy.append([pixel_x,pixel_y])
resistance_width = width_xy[-1][1] - width_xy[0][1]
print("resistance_width:",resistance_width)

    #좌&우측값 구하기(=resistance_length)##########################################
length_xy = []
for i in range(cols):
    for j in range(rows):
        if img_bin[j][i] == 255:
            pixel_x = i
            pixel_y = j
            length_xy.append([pixel_x,pixel_y])
resistance_length = length_xy[-1][0] - length_xy[0][0]
print("resistance_length:",resistance_length)

resistance_rectangle_top = width_xy[0][1]
resistance_rectangle_bottom = width_xy[-1][1]
resistance_rectangle_left = length_xy[0][0]
resistance_rectangle_right = length_xy[-1][0]
print("resistance_rectangle_top:",resistance_rectangle_top)
print("resistance_rectangle_bottom:",resistance_rectangle_bottom)
print("resistance_rectangle_left:",resistance_rectangle_left)
print("resistance_rectangle_right:",resistance_rectangle_right)

img_rgb = cv2.rectangle(img,(resistance_rectangle_left,resistance_rectangle_top),
                    (resistance_rectangle_right,resistance_rectangle_bottom),(0,255,0),3)

#저항띠 라벨링 하기
    #1번째 띠자리 비율로 구하기(x=76, y=46정도)
check_point_1_x = (resistance_rectangle_right - resistance_rectangle_left) / 3.05
check_point_1_y = ((resistance_rectangle_bottom - resistance_rectangle_top) / 2) + resistance_rectangle_top
img_rgb = cv2.circle(img,(int(check_point_1_x),int(check_point_1_y)), 5, (255,0,0), 3)

    #2번째 띠자리 비율로 구하기(x=103, y=46정도)
check_point_2_x = (resistance_rectangle_right - resistance_rectangle_left) / 2.30
check_point_2_y = ((resistance_rectangle_bottom - resistance_rectangle_top) / 2) + resistance_rectangle_top
img_rgb = cv2.circle(img,(int(check_point_2_x),int(check_point_2_y)), 5, (255,0,0), 3)

    #3번째 띠자리 비율로 구하기(x=130, y=46정도)
check_point_3_x = (resistance_rectangle_right - resistance_rectangle_left) / 1.83
check_point_3_y = ((resistance_rectangle_bottom - resistance_rectangle_top) / 2) + resistance_rectangle_top
img_rgb = cv2.circle(img,(int(check_point_3_x),int(check_point_3_y)), 5, (255,0,0), 3)

#색깔 추출(3x3픽셀 합쳐서 평균)
#1번째 띠 색깔 추출
print("check_point_1_center_bgr:",img[int(check_point_1_y)][int(check_point_1_x)])
    #1번째 띠 블루성분 추출
top_blue_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)]
top_blue_cp1 = int(top_blue_cp1[0])
top_left_blue_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)-1]
top_left_blue_cp1 = int(top_left_blue_cp1[0])
top_right_blue_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)+1]
top_right_blue_cp1 = int(top_right_blue_cp1[0])
center_blue_cp1 = img[int(check_point_1_y)][int(check_point_1_x)]
center_blue_cp1 = int(center_blue_cp1[0])
center_left_blue_cp1 = img[int(check_point_1_y)][int(check_point_1_x)-1]
center_left_blue_cp1 = int(center_left_blue_cp1[0])
center_right_blue_cp1 = img[int(check_point_1_y)][int(check_point_1_x)+1]
center_right_blue_cp1 = int(center_right_blue_cp1[0])
bottom_blue_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)]
bottom_blue_cp1 = int(bottom_blue_cp1[0])
bottom_left_blue_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)-1]
bottom_left_blue_cp1 = int(bottom_left_blue_cp1[0])
bottom_right_blue_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)+1]
bottom_right_blue_cp1 = int(bottom_right_blue_cp1[0])
    #1번째 띠 그린성분 추출
top_green_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)]
top_green_cp1 = int(top_green_cp1[1])
top_left_green_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)-1]
top_left_green_cp1 = int(top_left_green_cp1[1])
top_right_green_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)+1]
top_right_green_cp1 = int(top_right_green_cp1[1])
center_green_cp1 = img[int(check_point_1_y)][int(check_point_1_x)]
center_green_cp1 = int(center_green_cp1[1])
center_left_green_cp1 = img[int(check_point_1_y)][int(check_point_1_x)-1]
center_left_green_cp1 = int(center_left_green_cp1[1])
center_right_green_cp1 = img[int(check_point_1_y)][int(check_point_1_x)+1]
center_right_green_cp1 = int(center_right_green_cp1[1])
bottom_green_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)]
bottom_green_cp1 = int(bottom_green_cp1[1])
bottom_left_green_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)-1]
bottom_left_green_cp1 = int(bottom_left_green_cp1[1])
bottom_right_green_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)+1]
bottom_right_green_cp1 = int(bottom_right_green_cp1[1])
    #1번째 띠 레드성분 추출
top_red_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)]
top_red_cp1 = int(top_red_cp1[2])
top_left_red_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)-1]
top_left_red_cp1 = int(top_left_red_cp1[2])
top_right_red_cp1 = img[int(check_point_1_y)-1][int(check_point_1_x)+1]
top_right_red_cp1 = int(top_right_red_cp1[2])
center_red_cp1 = img[int(check_point_1_y)][int(check_point_1_x)]
center_red_cp1 = int(center_red_cp1[2])
center_left_red_cp1 = img[int(check_point_1_y)][int(check_point_1_x)-1]
center_left_red_cp1 = int(center_left_red_cp1[2])
center_right_red_cp1 = img[int(check_point_1_y)][int(check_point_1_x)+1]
center_right_red_cp1 = int(center_right_red_cp1[2])
bottom_red_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)]
bottom_red_cp1 = int(bottom_red_cp1[2])
bottom_left_red_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)-1]
bottom_left_red_cp1 = int(bottom_left_red_cp1[2])
bottom_right_red_cp1 = img[int(check_point_1_y)+1][int(check_point_1_x)+1]
bottom_right_red_cp1 = int(bottom_right_red_cp1[2])
    #1번째띠 3x3 bgr평균
average_blue_cp1 = (top_blue_cp1 + top_left_blue_cp1 + top_right_blue_cp1
                    + center_blue_cp1 + center_left_blue_cp1 + center_right_blue_cp1
                    + bottom_blue_cp1 + bottom_left_blue_cp1 + bottom_right_blue_cp1) / 9
average_green_cp1 = (top_green_cp1 + top_left_green_cp1 + top_right_green_cp1
                    + center_green_cp1 + center_left_green_cp1 + center_right_green_cp1
                    + bottom_green_cp1 + bottom_left_green_cp1 + bottom_right_green_cp1) / 9
average_red_cp1 = (top_red_cp1 + top_left_red_cp1 + top_right_red_cp1
                    + center_red_cp1 + center_left_red_cp1 + center_right_red_cp1
                    + bottom_red_cp1 + bottom_left_red_cp1 + bottom_right_red_cp1) / 9

    #1번째띠 bgr 출력
print("average_blue_cp1:",average_blue_cp1)
print("average_green_cp1:",average_green_cp1)
print("average_red_cp1:",average_red_cp1)
img_rgb = cv2.circle(img_rgb,(int(check_point_1_x),rows-10), 5, (int(average_blue_cp1),int(average_green_cp1),int(average_red_cp1)), -1)

#2번째 띠 색깔 추출
print("check_point_2_center_bgr:",img[int(check_point_2_y)][int(check_point_2_x)])
    #2번째 띠 블루성분 추출
top_blue_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)]
top_blue_cp2 = int(top_blue_cp2[0])
top_left_blue_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)-1]
top_left_blue_cp2 = int(top_left_blue_cp2[0])
top_right_blue_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)+1]
top_right_blue_cp2 = int(top_right_blue_cp2[0])
center_blue_cp2 = img[int(check_point_2_y)][int(check_point_2_x)]
center_blue_cp2 = int(center_blue_cp2[0])
center_left_blue_cp2 = img[int(check_point_2_y)][int(check_point_2_x)-1]
center_left_blue_cp2 = int(center_left_blue_cp2[0])
center_right_blue_cp2 = img[int(check_point_2_y)][int(check_point_2_x)+1]
center_right_blue_cp2 = int(center_right_blue_cp2[0])
bottom_blue_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)]
bottom_blue_cp2 = int(bottom_blue_cp2[0])
bottom_left_blue_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)-1]
bottom_left_blue_cp2 = int(bottom_left_blue_cp2[0])
bottom_right_blue_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)+1]
bottom_right_blue_cp2 = int(bottom_right_blue_cp2[0])
    #2번째 띠 그린성분 추출
top_green_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)]
top_green_cp2 = int(top_green_cp2[1])
top_left_green_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)-1]
top_left_green_cp2 = int(top_left_green_cp2[1])
top_right_green_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)+1]
top_right_green_cp2 = int(top_right_green_cp2[1])
center_green_cp2 = img[int(check_point_2_y)][int(check_point_2_x)]
center_green_cp2 = int(center_green_cp2[1])
center_left_green_cp2 = img[int(check_point_2_y)][int(check_point_2_x)-1]
center_left_green_cp2 = int(center_left_green_cp2[1])
center_right_green_cp2 = img[int(check_point_2_y)][int(check_point_2_x)+1]
center_right_green_cp2 = int(center_right_green_cp2[1])
bottom_green_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)]
bottom_green_cp2 = int(bottom_green_cp2[1])
bottom_left_green_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)-1]
bottom_left_green_cp2 = int(bottom_left_green_cp2[1])
bottom_right_green_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)+1]
bottom_right_green_cp2 = int(bottom_right_green_cp2[1])
    #2번째 띠 레드성분 추출
top_red_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)]
top_red_cp2 = int(top_red_cp2[2])
top_left_red_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)-1]
top_left_red_cp2 = int(top_left_red_cp2[2])
top_right_red_cp2 = img[int(check_point_2_y)-1][int(check_point_2_x)+1]
top_right_red_cp2 = int(top_right_red_cp2[2])
center_red_cp2 = img[int(check_point_2_y)][int(check_point_2_x)]
center_red_cp2 = int(center_red_cp2[2])
center_left_red_cp2 = img[int(check_point_2_y)][int(check_point_2_x)-1]
center_left_red_cp2 = int(center_left_red_cp2[2])
center_right_red_cp2 = img[int(check_point_2_y)][int(check_point_2_x)+1]
center_right_red_cp2 = int(center_right_red_cp2[2])
bottom_red_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)]
bottom_red_cp2 = int(bottom_red_cp2[2])
bottom_left_red_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)-1]
bottom_left_red_cp2 = int(bottom_left_red_cp2[2])
bottom_right_red_cp2 = img[int(check_point_2_y)+1][int(check_point_2_x)+1]
bottom_right_red_cp2 = int(bottom_right_red_cp2[2])
    #2번째띠 3x3 bgr평균
average_blue_cp2 = (top_blue_cp2 + top_left_blue_cp2 + top_right_blue_cp2
                    + center_blue_cp2 + center_left_blue_cp2 + center_right_blue_cp2
                    + bottom_blue_cp2 + bottom_left_blue_cp2 + bottom_right_blue_cp2) / 9
average_green_cp2 = (top_green_cp2 + top_left_green_cp2 + top_right_green_cp2
                    + center_green_cp2 + center_left_green_cp2 + center_right_green_cp2
                    + bottom_green_cp2 + bottom_left_green_cp2 + bottom_right_green_cp2) / 9
average_red_cp2 = (top_red_cp2 + top_left_red_cp2 + top_right_red_cp2
                    + center_red_cp2 + center_left_red_cp2 + center_right_red_cp2
                    + bottom_red_cp2 + bottom_left_red_cp2 + bottom_right_red_cp2) / 9

    #2번째띠 bgr 출력
print("average_blue_cp2:",average_blue_cp2)
print("average_green_cp2:",average_green_cp2)
print("average_red_cp2:",average_red_cp2)
img_rgb = cv2.circle(img_rgb,(int(check_point_2_x),rows-10), 5, (int(average_blue_cp2),int(average_green_cp2),int(average_red_cp2)), -1)

#3번째 띠 색깔 추출
print("check_point_3_center_bgr:",img[int(check_point_3_y)][int(check_point_3_x)])
    #3번째 띠 블루성분 추출
top_blue_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)]
top_blue_cp3 = int(top_blue_cp3[0])
top_left_blue_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)-1]
top_left_blue_cp3 = int(top_left_blue_cp3[0])
top_right_blue_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)+1]
top_right_blue_cp3 = int(top_right_blue_cp3[0])
center_blue_cp3 = img[int(check_point_3_y)][int(check_point_3_x)]
center_blue_cp3 = int(center_blue_cp3[0])
center_left_blue_cp3 = img[int(check_point_3_y)][int(check_point_3_x)-1]
center_left_blue_cp3 = int(center_left_blue_cp3[0])
center_right_blue_cp3 = img[int(check_point_3_y)][int(check_point_3_x)+1]
center_right_blue_cp3 = int(center_right_blue_cp3[0])
bottom_blue_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)]
bottom_blue_cp3 = int(bottom_blue_cp3[0])
bottom_left_blue_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)-1]
bottom_left_blue_cp3 = int(bottom_left_blue_cp3[0])
bottom_right_blue_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)+1]
bottom_right_blue_cp3 = int(bottom_right_blue_cp3[0])
    #3번째 띠 그린성분 추출
top_green_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)]
top_green_cp3 = int(top_green_cp3[1])
top_left_green_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)-1]
top_left_green_cp3 = int(top_left_green_cp3[1])
top_right_green_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)+1]
top_right_green_cp3 = int(top_right_green_cp3[1])
center_green_cp3 = img[int(check_point_3_y)][int(check_point_3_x)]
center_green_cp3 = int(center_green_cp3[1])
center_left_green_cp3 = img[int(check_point_3_y)][int(check_point_3_x)-1]
center_left_green_cp3 = int(center_left_green_cp3[1])
center_right_green_cp3 = img[int(check_point_3_y)][int(check_point_3_x)+1]
center_right_green_cp3 = int(center_right_green_cp3[1])
bottom_green_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)]
bottom_green_cp3 = int(bottom_green_cp3[1])
bottom_left_green_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)-1]
bottom_left_green_cp3 = int(bottom_left_green_cp3[1])
bottom_right_green_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)+1]
bottom_right_green_cp3 = int(bottom_right_green_cp3[1])
    #3번째 띠 레드성분 추출
top_red_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)]
top_red_cp3 = int(top_red_cp3[2])
top_left_red_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)-1]
top_left_red_cp3 = int(top_left_red_cp3[2])
top_right_red_cp3 = img[int(check_point_3_y)-1][int(check_point_3_x)+1]
top_right_red_cp3 = int(top_right_red_cp3[2])
center_red_cp3 = img[int(check_point_3_y)][int(check_point_3_x)]
center_red_cp3 = int(center_red_cp3[2])
center_left_red_cp3 = img[int(check_point_3_y)][int(check_point_3_x)-1]
center_left_red_cp3 = int(center_left_red_cp3[2])
center_right_red_cp3 = img[int(check_point_3_y)][int(check_point_3_x)+1]
center_right_red_cp3 = int(center_right_red_cp3[2])
bottom_red_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)]
bottom_red_cp3 = int(bottom_red_cp3[2])
bottom_left_red_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)-1]
bottom_left_red_cp3 = int(bottom_left_red_cp3[2])
bottom_right_red_cp3 = img[int(check_point_3_y)+1][int(check_point_3_x)+1]
bottom_right_red_cp3 = int(bottom_right_red_cp3[2])
    #3번째띠 3x3 bgr평균
average_blue_cp3 = (top_blue_cp3 + top_left_blue_cp3 + top_right_blue_cp3
                    + center_blue_cp3 + center_left_blue_cp3 + center_right_blue_cp3
                    + bottom_blue_cp3 + bottom_left_blue_cp3 + bottom_right_blue_cp3) / 9
average_green_cp3 = (top_green_cp3 + top_left_green_cp3 + top_right_green_cp3
                    + center_green_cp3 + center_left_green_cp3 + center_right_green_cp3
                    + bottom_green_cp3 + bottom_left_green_cp3 + bottom_right_green_cp3) / 9
average_red_cp3 = (top_red_cp3 + top_left_red_cp3 + top_right_red_cp3
                    + center_red_cp3 + center_left_red_cp3 + center_right_red_cp3
                    + bottom_red_cp3 + bottom_left_red_cp3 + bottom_right_red_cp3) / 9

    #3번째띠 bgr 출력
print("average_blue_cp3:",average_blue_cp3)
print("average_green_cp3:",average_green_cp3)
print("average_red_cp3:",average_red_cp3)
img_rgb = cv2.circle(img_rgb,(int(check_point_3_x),rows-10), 5, (int(average_blue_cp3),int(average_green_cp3),int(average_red_cp3)), -1)






#결과 확인
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(1,2,1), plt.imshow(img_rgb), plt.title('img_rgb')
plt.subplot(1,2,2), plt.imshow(img_bin), plt.title('img_bin')
plt.show()






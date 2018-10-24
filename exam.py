import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread('C:/Users/301ST-28/PycharmProjects/vision/logo2.jpg', cv2.IMREAD_COLOR)

# 삽입할 이미지의 row, col, channel정보
rows, cols, channels = img.shape

img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

while(True):
    # ret : frame capture결과(boolean)
    # frame : Capture한 frame
    ret, frame = cap.read()

    if (ret):
        # 대상 이미지에서 삽입할 이미지의 영역을 추출
        roi = frame[0:rows, 0:cols]
        # bitwise_and 연산자는 둘다 0이 아닌 경우만 값을 통과 시킴.
        img1_fg = cv2.bitwise_and(img, img, mask=mask_inv)
        img2_bg = cv2.bitwise_and(roi, roi, mask=mask)
        # 2개의 이미지를 합치면 바탕은 제거되고 logo부분만 합쳐짐.
        dst = cv2.add(img1_fg, img2_bg)
        # 합쳐진 이미지를 원본 이미지에 추가.
        frame[0:rows, 0:cols] = dst

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
import random
import time


#선: cv2.line(image, (top, left), (bottom, right), (B, G, R), thickness)
#사각형: cv2.Rectangle(image, (top, left), (bottom, right), (B, G, R), thickness)
#원: cv2.Circle (image, (x, y), radius, (B, G, R), thickness)
#호: cv2.ellipse(image, (x, y), axes, angle, startAngle, endAngle, (B, G, R), thickness)
#다각형: cv2.polylines(image, array[], isClosed, (B, G, R))
#문자열: cv2.putText(image, String, point(x,y), font, scale, (B,G,R), thickness, type)
def func1(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (255, 0, 0), 3)

img = np.zeros([512,512,3], np.uint8)
cv2.namedWindow('JPRO')
cv2.setMouseCallback('JPRO', func1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Finish: ESC',(80,500), font, 2,(255,255,255),2,cv2.LINE_AA)

level = 0
easy = 9
normal = 6
hard = 3

while True:
    cv2.imshow('JPRO', img)
    a = random.randrange(0,511)
    b = random.randrange(0,511)
    c = random.randrange(0,255)
    d = random.randrange(0,255)
    e = random.randrange(0,255)
    level = level + 1
    time.sleep(0.1)
    if level is normal:
        cv2.circle(img, (a, b), 10, (c, d, e), -1)
        level = 0

    if cv2.waitKey(20) & 0xFF == 27:
        break


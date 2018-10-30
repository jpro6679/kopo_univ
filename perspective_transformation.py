import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('timetable.png')
rows,cols,ch = img.shape

pts1 = np.float32([[217,228],[394,192],[254,427],[432,391]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

img = cv2.circle(img,(pts1[0][0],pts1[0][1]), 10, (255,0,0), -1)
img = cv2.circle(img,(pts1[1][0],pts1[1][1]), 10, (255,0,0), -1)
img = cv2.circle(img,(pts1[2][0],pts1[2][1]), 10, (255,0,0), -1)
img = cv2.circle(img,(pts1[3][0],pts1[3][1]), 10, (255,0,0), -1)

M = cv2.getPerspectiveTransform(pts1,pts2) # 4x2 matrix

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(211),plt.imshow(img),plt.title('Input')
plt.subplot(212),plt.imshow(dst),plt.title('Output')
plt.show()

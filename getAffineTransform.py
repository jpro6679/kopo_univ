import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('flippy.jpg')
# img = cv2.circle(img,(50,50), 10, (255,0,0), -1)
# img = cv2.circle(img,(200,50), 10, (255,0,0), -1)
# img = cv2.circle(img,(50,200), 10, (255,0,0), -1)
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
#########################################################################
img = cv2.circle(img,(pts1[0][0],pts1[0][1]), 10, (255,0,0), -1)
img = cv2.circle(img,(pts1[1][0],pts1[1][1]), 10, (255,0,0), -1)
img = cv2.circle(img,(pts1[2][0],pts1[2][1]), 10, (255,0,0), -1)
#########################################################################
M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

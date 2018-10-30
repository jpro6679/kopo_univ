import cv2
import numpy as np

#엣지 검출할 그레이사진 하나, BGR값 찾을 칼라사진 하나
img = cv2.imread('all.jpg')
img2 = cv2.imread('all.jpg',0)
img3 = img2 + img2 + img2
img4 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img5 = img4 - img4 - img4
img6 = cv2.cvtColor(img5,cv2.COLOR_HSV2BGR)
img7 = cv2.cvtColor(img6,cv2.COLOR_BGR2GRAY)

#choice1. sobel -> 탈락
# kernel = np.ones((3,3),np.float32)/9
# dst = cv2.filter2D(img2,-1,kernel)
# kernel2 = np.ones((5,5),np.float32)/25
# dst2 = cv2.filter2D(img2,-1,kernel2)
# kernel3 = np.ones((7,7),np.float32)/49
# dst3 = cv2.filter2D(img2,-1,kernel3)
#
# sobelx = cv2.Sobel(dst3,cv2.CV_64F,1,0,ksize=3)
# sobelx2 = cv2.Sobel(dst3,cv2.CV_64F,1,0,ksize=5)
# sobelx3 = cv2.Sobel(dst3,cv2.CV_64F,1,0,ksize=7)
# sobely = cv2.Sobel(dst3,cv2.CV_64F,0,1,ksize=3)
# sobely2 = cv2.Sobel(dst3,cv2.CV_64F,0,1,ksize=5)
# sobely3 = cv2.Sobel(dst3,cv2.CV_64F,0,1,ksize=7)
#
# j = sobelx + sobely
# j2 = sobelx2 + sobely2
# j3 = sobelx3 + sobely3

#choice2. laplacian
# kernel = np.ones((3,3),np.float32)/9
# dst = cv2.filter2D(img2,-1,kernel)
# kernel2 = np.ones((5,5),np.float32)/25
# dst2 = cv2.filter2D(img2,-1,kernel2)
# kernel3 = np.ones((7,7),np.float32)/49
# dst3 = cv2.filter2D(img2,-1,kernel3)
#
# j = cv2.Laplacian(dst,cv2.CV_64F)
# j2 = cv2.Laplacian(dst2,cv2.CV_64F)
# j3 = cv2.Laplacian(dst3,cv2.CV_64F)

#Choice3. Canny Edge Detection
edges = cv2.Canny(img4, 100, 200)
print(edges)

#result.
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.imshow('img2',img2)
cv2.imshow('edges',edges)
cv2.imshow('img5',img5)
cv2.imshow('img7',img7)

# cv2.imshow('dst',j)
# cv2.imshow('dst2', j2)
# cv2.imshow('dst3', j3)
cv2.waitKey(0)
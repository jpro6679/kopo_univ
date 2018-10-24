# import cv2
# import numpy as np
#
# img = cv2.imread('C:/py_vision/jim_sniper2.jpg', 0) # 이미지를 img변수에 입력한다.
# rows,cols = img.shape # 이미지의 행과, 열을 rows와 cols에 넣는다.
#
# M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
# dst = cv2.warpAffine(img, M, (cols,rows)) # translation된 dst변수
# N = np.float32([[1,0,50],[0,1,50]]) # translation M matrix
# dst = cv2.warpAffine(dst, N, (cols,rows)) # translation된 dst변수
#
# cv2.imshow('img',img)
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv2.imread('C:/py_vision/jim_sniper2.jpg')
# rows,cols,ch = img.shape
#
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
#
# M = cv2.getAffineTransform(pts1,pts2)
#
# dst = cv2.warpAffine(img,M,(cols,rows))
#
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()




import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/py_vision/jim_sniper2.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(211),plt.imshow(img),plt.title('Input')
plt.subplot(212),plt.imshow(dst),plt.title('Output')
plt.show()

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while (cap.isOpened()):
    ret, frame = cap.read()
    # if ret == True:
        # frame = cv2.flip(frame,0) # 0 or 1
    cv2.waitKey(10)
    out.write(frame)
    cv2.imshow('frame', frame)

    # else:
    #     break

cap.release()
out.release()
cv2.destroyAllWindows()

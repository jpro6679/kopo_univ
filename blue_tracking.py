import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    #Capture frame by frame###############################
    _, frame = cap.read()


    #frame rows&cols information############################
    rows, cols, _ = frame.shape
    #print(rows, cols) # rows:480, cols:640

    #convert hsv for image thresholding###################
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #define range of red color in hsv######################
    lower_blue = np.array([100,150,50])
    upper_blue = np.array([125,255,255])

    #threshold hsv image to get only red colors################
    frame_bin = cv2.inRange(frame_hsv,lower_blue,upper_blue)




    #convert gray for using contours function######################
    # frame_gray1 = cv2.cvtColor(frame_bin,cv2.COLOR_HSV2GRAY)
    # frame_gray2 = cv2.cvtColor(frame_bin,cv2.COLOR_HSV2GRAY)

    #find contour
    _, contours, _ = cv2.findContours(frame_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #draw contour
    max_area = []
    temp = []
    for i in range(len(contours)):
        max_area.append(cv2.contourArea(contours[i]))
        temp.append(cv2.contourArea(contours[i]))

    max_area.sort(reverse=True)
    for i in range(len(contours)):
        if temp[i] == max_area[0]:
            index = i
            break

    cv2.drawContours(frame, contours, index, (0, 255, 0), 3)

    #draw center point
    M = cv2.moments(contours[index])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.circle(frame, (cx,cy), 20, (0,0,255), -1)





    #find center(x,y) using moment function
    # M = cv2.moments(contours[i])
    # print(M)
    # if M['m10'] != 0:
    #     cx = int(M['m10']/M['m00'])
    #     cy = int(M['m01']/M['m00'])

    # frame = cv2.circle(frame, (cx, cy), 50, (0, 0, 255), -1)

    # bottom = contours[0] #좌표임
    # top = contours[-1] #좌표임
    # left = contours[int(len(contours)/4)]
    # right = contours[int(len(contours)/4*3)]

    # print("bottom:",bottom[0][0][0])
    # print("top:",top[0][0][0])
    # print("left:",left[0][0][0])
    # print("right:",right[0][0][0])

    # frame = cv2.rectangle(frame, (top[0][0][0], left[0][0][0]), (bottom[0][0][0], right[0][0][0]), (0, 255, 0), 3)




    #result
    cv2.imshow('frame', frame)



    if cv2.waitKey(1) & 0xFF == 27:
        break

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
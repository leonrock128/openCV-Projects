import cv2
import numpy as np

circles = np.zeros((4,2),np.int32)
count = 0

def mousePoints(event,x,y,flags,params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,y)
        circles[count] = x,y
        count +=1
        print(circles)

img = cv2.imread("openCV/bear.jpg")
img = cv2.resize(img,(900,600))

while True:

    if count == 4:

        width,height = 250,350
        pt1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

        matx = cv2.getPerspectiveTransform(pt1,pt2)
        op = cv2.warpPerspective(img,matx,(width,height))
        cv2.imshow("Output Image",op)

    for i in range(0,4):
        cv2.circle(img,(int(circles[i][0]),int(circles[i][1])),5,(0,0,255),cv2.FILLED)
        # cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)

    cv2.imshow("Orginial Image",img)
    cv2.setMouseCallback("Orginial Image",mousePoints) # here detect mouse click points
    
    cv2.waitKey(1)
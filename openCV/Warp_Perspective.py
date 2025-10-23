import cv2
import numpy as np


img = cv2.imread("openCV/resize_tree.jpg")
# img = cv2.resize(img,(900,506))

width,height = 200,423
pt1 = np.float32([[390,100],[595,100],[390,490],[615,490]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


for i in range(0,4):

    # cv2.circle(img,(tuple(map(int,pt1[i][0])),tuple(map(int,pt1[i][1]))),5,(0,0,255),cv2.FILLED)
    cv2.circle(img,(int(pt1[i][0]),int(pt1[i][1])),5,(0,0,255),cv2.FILLED)


cv2.imshow("Orginial Image",img)
cv2.imshow("Output Image",imgOutput)
cv2.waitKey(0)


 

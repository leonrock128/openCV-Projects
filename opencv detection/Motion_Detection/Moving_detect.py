import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret,frame1 = cap.read()
ret,frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(21,21),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh,None,iterations=2)
    contour,_ = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1,contour,-1,(0,255,0),2)

    for cnt in contour:
        x,y,h,w  = cv2.boundingRect(cnt)

        if cv2.contourArea(cnt) < 200:
            continue
        cv2.rectangle(frame1,(x,y),(x+h,y+w),(0,255,0),2)
        cv2.putText(frame1,"Status: {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3) # img, text , origin , fontFace , fontScale , color , thickness= none, lineType = none, bottomLeftOrigin = None



    cv2.imshow("web camp",frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(2) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
       
 



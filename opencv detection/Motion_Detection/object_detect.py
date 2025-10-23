import cv2,time

video = cv2.VideoCapture(0) # here we use camera instead of 0 value eg:'vtest.avi'
frist_frame = None

while video.isOpened(): # while True: 
    ret,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    if frist_frame is None:
        frist_frame = gray
        continue
    delta_frame = cv2.absdiff(frist_frame,gray)
    threshold_frame = cv2.threshold(delta_frame,50,255,cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame,None,iterations=2 )
    (contour,_) = cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
     
    for cnt in contour:
        
        if cv2.contourArea(cnt) < 700:
            continue
        x,y,h,w = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),3)

    cv2.imshow("web cam",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()





       


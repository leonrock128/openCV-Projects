import os
import cv2

# f_width = 700
# f_height = 500
#read video
# video_path = os.path.join('.','data','openCV/power_star.mp4')
video = cv2.VideoCapture('.//openCV//power_star.mp4')
# video = cv2.resize(video1,(500,500))

#visualize video
ret = True
while ret:
    ret, frame = video.read()
    img = cv2.resize(frame,(800,500))

    if ret:
        cv2.imshow('frame',img)
        cv2.waitKey(40)
video.release()
cv2.destroyAllWindows(40)


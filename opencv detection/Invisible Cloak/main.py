# Current frame - bedsheet + first frame = Invisible cloak
import cv2
import numpy as np

def empty(x):
    pass

cap = cv2.VideoCapture(0)
bars = cv2.namedWindow("bars")

cv2.createTrackbar("U_hue","bars",110,180,empty)
cv2.createTrackbar("U_sat","bars",255,255,empty)
cv2.createTrackbar("U_val","bars",255,255,empty)
cv2.createTrackbar("L_hue","bars",68,180,empty)
cv2.createTrackbar("L_sat","bars",55,255,empty)
cv2.createTrackbar("L_val","bars",54,255,empty)

# Capturing the initial frame for creation of background
while True:
    cv2.waitKey(1000)
    ret,int_frame = cap.read()
    if(ret):
        break

# Start capturing the frames for actual magic!
while True:
    ret,frame =cap.read()
    inspect = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #  getting the HSV values for masking the cloak
    u_hue = cv2.getTrackbarPos("U_hue","bars")
    u_sat = cv2.getTrackbarPos("U_sat","bars")
    u_val = cv2.getTrackbarPos("U_val","bars")
    l_hue = cv2.getTrackbarPos("L_hue","bars")
    l_sat = cv2.getTrackbarPos("L_sat","bars")
    l_val = cv2.getTrackbarPos("L_val","bars")

    kernal = np.ones((3,3),np.uint8)
    upper_hsv = np.array([u_hue,u_sat,u_val])
    lower_hsv = np.array([l_hue,l_sat,l_val])

    mask = cv2.inRange(inspect,lower_hsv,upper_hsv)
    mask = cv2.medianBlur(mask,3)
    mask_inv = 255-mask
    mask = cv2.dilate(mask,kernal,5)

    # mixing of frames in a combination to acheive the required frame
    b = frame[:,:,0]
    g = frame[:,:,1]
    r = frame[:,:,2]
    b = cv2.bitwise_and(mask_inv,b)
    g = cv2.bitwise_and(mask_inv,g)
    r = cv2.bitwise_and(mask_inv,r)
    frame_inv = cv2.merge((b,g,r))

    b = int_frame[:,:,0]
    g = int_frame[:,:,1]
    r = int_frame[:,:,2]
    b = cv2.bitwise_and(b,mask)
    g = cv2.bitwise_and(g,mask)
    r = cv2.bitwise_and(r,mask)
    blanket_area = cv2.merge((b,g,r))

    final = cv2.bitwise_or(frame_inv,blanket_area)
    cv2.imshow("Invisible",final)

    if(cv2.waitKey(3) == ord('q')):
        break;

cv2.destroyAllWindows()
cap.release()
#resizing
import os
import cv2

img = cv2.imread(os.path.join('.','openCV/bear.jpg'))

resized_img = cv2.resize(img,(500,500))

# print(img.shape)
print(resized_img.shape)

# cv2.imshow('image',img)
cv2.imshow('resized_img',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# mouse drawing
'''import cv2  
import numpy as np  
draw = False # true if the mouse is pressed. Press m to shift into curve mode.  
mode = True # if True, draw rectangle.  
a,b = -1,-1  
# mouse callback function  
def draw_circle(event,x,y,flags,param):  
    global a,b,draw,mode  
    if(event == cv2.EVENT_LBUTTONDOWN):  
        draw = True  
        a,b = x,y  
    elif (event == cv2.EVENT_MOUSEMOVE):  
        if draw == True:  
            if mode == True:  
                cv2.rectangle(img,(a,b),(x,y),(0,255,0),-1)  
            else:  
                cv2.circle(img,(x,y),5,(0,0,255),-1)  
    elif(event == cv2.EVENT_LBUTTONUP):  
        draw = False  
        if mode == True:  
            cv2.rectangle(img,(a,b),(x,y),(0,255,0),-1)  
        else:  
            cv2.circle(img,(x,y),5,(0,0,255),-1)  
# We bind the keyboard key m to toggle between rectangle and circle.  
img = np.zeros((512,512,3), np.uint8)  
cv2.namedWindow('image')  
cv2.setMouseCallback('image',draw_circle)  
while(1):  
    cv2.imshow('image',img)  
    k = cv2.waitKey(1) & 0xFF  
    if k == ord('m'):  
        mode = not mode  
    elif(k == 27):  
        break  
cv2.destroyAllWindows() ''' 
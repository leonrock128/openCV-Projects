import os 
import cv2

img = cv2.imread(os.path.join('.','openCV/bear.jpg'))
img_resize = cv2.resize(img,(500,500))

img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)

# global_threshold
# ret,thresh = cv2.threshold(img_gray,90,255,cv2.THRESH_BINARY)

#adaptive_threshold
adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,3)

ret,simple_thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)


cv2.imshow("Image",img_resize)
cv2.imshow("thresh",adaptive_thresh)
cv2.imshow("simple_thresh",simple_thresh)
cv2.waitKey(0)
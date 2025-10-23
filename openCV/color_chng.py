import os
import cv2

img = cv2.imread(os.path.join('.' , 'openCV/bear.jpg'))
img_resize = cv2.resize(img,(500,500))

img_rgb = cv2.cvtColor(img_resize,cv2.COLOR_BGR2RGBA)
img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
img_hsb = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)

cv2.imshow("image",img)
cv2.imshow("Image",img_resize)
cv2.imshow("image",img_rgb)
cv2.imshow("gray",img_gray)
cv2.imshow("hsb",img_hsb)
cv2.waitKey(0)
import os
import cv2

img = cv2.imread(os.path.join('.','openCV/bear.jpg'))
img_resize = cv2.resize(img,(500,500))

print(img_resize.shape)

#line
cv2.line(img_resize,(100,150),(300,450),(0,255,0),3)

#rectangle
cv2.rectangle(img_resize,(200,350),(350,400),(0,0,255),6)
#fill with color due to -1
# cv2.rectangle(img_resize,(200,350),(350,400),(0,0,255),-1)

#circle
cv2.circle(img_resize,(200,350),75,(255,0,0),10)

#text
cv2.putText(img_resize,"Hello",(200,350),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,0),10)

cv2.imshow('Image',img_resize)
cv2.waitKey(0)
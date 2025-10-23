import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.','openCV/tree.jpg'))
img_resize = cv2.resize(img,(500,500))

img_edge = cv2.Canny(img_resize,350,600)

#dilate
img_edge_d = cv2.dilate(img_edge,np.ones((5,5),dtype=np.int8))

#erode()
img_edge_e = cv2.erode(img_edge_d,np.ones((5,5),dtype=np.int8))


cv2.imshow("Image",img_resize)
cv2.imshow("edge image",img_edge)
cv2.imshow("edge_d",img_edge_d)
cv2.imshow("edge_e",img_edge_e)
cv2.waitKey(0)

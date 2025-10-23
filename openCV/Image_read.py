import os
import numpy as np
import cv2

#read image
# image_path = os.path.join('.', 'data', 'bear.jpg')

valu1 = cv2.imread('.\openCV/bear.jpg')
# print(val)
valu1 = cv2.resize(valu1,(500,500))

valu2 = cv2.imread('.\openCV/tree.jpg')
resized2 = cv2.resize(valu2,(500,500))

hor = np.hstack((valu1,resized2))
ver = np.vstack((valu1,resized2))
#write image

#Apply Gaussian blur
# blurred_image = cv2.GaussianBlur(valu,(5,5),0)

# cv2.imwrite(os.path.join('.', 'data', 'logo_read.png'), val)
# cv2.imwrite('Image_cv2/logo_read.png',valu)

#visualize image

# cv2.imshow("Blurred Image",blurred_image)

# cv2.imshow("image", valu)
cv2.imshow("resized_image",valu1)
cv2.imshow("vertical_image",ver)
cv2.imshow("horizontal_image",hor)
cv2.waitKey(0)

cv2.destroyAllWindows()


import os
import cv2

img = cv2.imread("openCV/bear.jpg")
img_resize = cv2.resize(img,(501,501))

cv2.imshow("image",img_resize)

#blur
k_size = 7
img_blur = cv2.blur(img_resize,(k_size,k_size))
img_gaussian_blur = cv2.GaussianBlur(img_resize,(k_size,k_size),5) 
img_median_blur = cv2.medianBlur(img_resize,k_size)


# cv2.imshow("image",img_resize)
cv2.imshow("image",img_blur)
cv2.imshow("guass Image",img_gaussian_blur)
cv2.imshow("Median Image",img_median_blur)
cv2.waitKey(0)
import os
import cv2

img = cv2.imread(os.path.join('.','openCV/bear.jpg'))
img_resize = cv2.resize(img,(500,500))

print(img.shape)

cropped_img = img_resize[50:550,10:500]  # height start with 50 and endwith 550 and width start with 10 and endwith 500

# cv2.imshow('image',img)
cv2.imshow('cropped_image',cropped_img)
cv2.waitKey(0)
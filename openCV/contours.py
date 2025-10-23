import os
import cv2

img= cv2.imread(os.path.join('.','openCV/tree.jpg'))
img_resize = cv2.resize(img,(500,500))

img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        # cv2.drawContours(img_resize,cnt,-1,(0,255,0),1)
        x1,y1,w,h = cv2.boundingRect(cnt)

        cv2.rectangle(img_resize,(x1,y1),(x1 + w,y1+h),(0,255,0),2)


# print(cv2.contourArea(cnt))

cv2.imshow("img_resize",img_resize)
cv2.imshow("img_gray",img_gray)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)

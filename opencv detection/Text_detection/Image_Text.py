import cv2
import os
import easyocr
import matplotlib.pyplot as plt
import numpy as np

'''outline
1.Take a look at the data
2. Extract text from images:
    -pytesseract here download tesseract file 
    -easyocr
    -keras_ocr  pip install keras-ocr -q __ it takes more time to excute the code
    '''
   
# read the image
img =  cv2.imread(os.path.join('.','opencv detection/Text_detection/image.png'))
img = cv2.resize(img,(600,500))

# instance text detector
reader = easyocr.Reader(['en'],gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25

# draw bbox and text
for i_,i in enumerate(text_):
    # print(i)
    bbox,text,score = i
    # print(bbox)
    # x1,x2,y1,y2 = []
    # bbox = [x1,x2,y1,y2]
    # coor = bbox[0]
    # c1,c2 = (coor[1],coor[0]),(coor[3],coor[2])
    if score > threshold:

        cv2.rectangle(img,tuple(map(int,bbox[0])),tuple(map(int,bbox[2])),(0,255,0),3)
        # cv2.rectangle(img,(0,255,0),2)
        cv2.putText(img,text,tuple(map(int,bbox[0])),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
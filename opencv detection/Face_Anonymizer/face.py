import os

import argparse

import cv2
import mediapipe as mp


def process_img(img,face_detection):

    H,W,_ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    # print(out.detections)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1,y1,w,h = bbox.xmin,bbox.ymin,bbox.width,bbox.height
            x1 = int(x1*W)
            y1 = int(y1*H)
            w = int(w*W)
            h= int(h*H)

            #here the rectangle around the face
            # img = cv2.rectangle(img,(x1,y1),(x1 + w,y1 + h),(0,255,0),3)


#blur Image
            if x1 >=0 and y1 >=0 and x1 + w <=img.shape[1] and y1 + h <= img.shape[0]:
                img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :],(30,30))

    return img

args = argparse.ArgumentParser()
# args.add_argument("--mode",default='image')
# args.add_argument("--filePath",default = "openCV/Face_Anonymizer/freecompress-Photo.jpg")

# args.add_argument("--mode",default='video')
# args.add_argument("--filePath",default = "opencv detection/Face_Anonymizer/power_star.mp4")

args.add_argument("--mode",default='webcam')
args.add_argument("--filePath",default = None)


args = args.parse_args()


output_dir = './output'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

'''img_path ='openCV/Face_Anonymizer/freecompress-Photo.jpg'

img = cv2.imread(img_path)
img_resize = cv2.resize(img,(500,500))

H,W,_ = img_resize.shape'''


#detect Image

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:

    if args.mode in ["image"]:
        #read image
        img = cv2.imread(args.filePath)
        img = cv2.resize(img,(500,500))

        # H,W,_ = img_resize.shape

        img = process_img(img,face_detection)

        #save Image
        cv2.imwrite(os.path.join(output_dir,"output.png"),img)
        # cv2.imshow("image",img_resize)

    elif args.mode in ["video"]:

        cap = cv2.VideoCapture(args.filePath)
        ret,frame = cap.read()
        frame = cv2.resize(frame,(600,600))

        
        output_video = cv2.VideoWriter(os.path.join(output_dir,"output.mp4"),cv2.VideoWriter_fourcc(*'MP4V'),25,(frame.shape[1],frame.shape[0]))

        while ret:
            frame = process_img(frame,face_detection)

            output_video.write(frame)
            
            ret, frame = cap.read()

        cap.release() 
        output_video.release()   

    elif args.mode in ['webcam']:
        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()

        while ret:
            frame = process_img(frame,face_detection)  
            cv2.imshow("frame",frame)
            cv2.waitKey(40)

            ret, frame = cap.read()
            
            if cv2.waitKey(40) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    '''img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    # print(out.detections)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1,y1,w,h = bbox.xmin,bbox.ymin,bbox.width,bbox.height
            x1 = int(x1*W)
            y1 = int(y1*H)
            w = int(w*W)
            h= int(h*H)

            #here the rectangle around the face
            # img_resize = cv2.rectangle(img_resize,(x1,y1),(x1 + w,y1 + h),(0,255,0),3)


#blur Image

img_resize[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img_resize[y1:y1 + h, x1:x1 + w, :],(30,30))'''


'''#save Image
cv2.imwrite(os.path.join(output_dir,"output.png"),img_resize)'''

    

# cv2.imshow("image",img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows(40)
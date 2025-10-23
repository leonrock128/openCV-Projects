import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

video=cv2.VideoCapture(0)

while True:
  check,frame=video.read()
  H, W, _ = frame.shape
  result = face_mesh.process(frame)
  # print(result)
  try:
    for facial_landmarks in result.multi_face_landmarks:
        for i in range(0,700):
            landmrk = facial_landmarks.landmark[i]

            '''bbox = landmrk.relative_bounding_box

            x1,y1,w,h = bbox.xmin,bbox.ymin,bbox.width,bbox.height
            x1 = int(x1*W)
            y1 = int(y1*H)
            w = int(w*W)
            h= int(h*H)'''

            locx = int(landmrk.x * W)
            locy = int(landmrk.y * H)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            cv2.circle(frame, (locx,locy),1,(0,200,0),0)

            # cv2.circle(frame, (x1,y1),(x1+h,y1+w),1,(0,200,0),0)

            cv2.imshow("Image",frame)
  except:
    cv2.imshow("Image",frame)
  key = cv2.waitKey(1)
  if key==ord('q'):
    break


video.release()
cv2.destroyAllWindows()


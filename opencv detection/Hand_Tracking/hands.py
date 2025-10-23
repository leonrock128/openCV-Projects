import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands
hand_mesh = hands.Hands(static_image_mode = True,min_detection_confidence = 0.7)


while True:
    ret,frame = cap.read()
    img_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # results = hands.process(img_rgb)

    cv2.imshow("Web camp" ,frame)

    if cv2.waitKey(2) == ord(
        'q'):
        break

cap.release()
cv2.destroyAllWindows()

    

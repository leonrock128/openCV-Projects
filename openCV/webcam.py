import cv2

# ip = input("Ip address of your phone: ")
#read webcam
webcam = cv2.VideoCapture(0)
# webcam = cv2.VideoCapture()
# webcam.set(3,700) # width 
# webcam.set(4,600) # height
# webcam.set(10,100) # brightness

#visualze webcam
while True:
    ret,frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

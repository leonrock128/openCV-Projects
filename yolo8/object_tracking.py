'''import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8n.pt")  # You can replace 'yolov8n.pt' with your model's path

# Load an image
image = cv2.imread("path_to_your_image.jpg")

# Perform object detection
results = model(image)

# Draw bounding boxes on the image
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the image
cv2.imshow("YOLO Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


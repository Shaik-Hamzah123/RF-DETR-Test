import cv2
import numpy as np
import json
from rfdetr import RFDETRBase

# Load the model
model = RFDETRBase()

# Read the classes.json file and store class names in a dictionary
with open('classes.json', 'r', encoding='utf-8') as file:
    class_names = json.load(file)

# Open the video file
cap = cv2.VideoCapture('walking.mp4')  # https://www.pexels.com/video/video-of-people-walking-855564/

# Create the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (960, 540))

# For live video streaming:
# cap = cv2.VideoCapture(0)  # 0 refers to the default camera

while True:
    # Read a frame
    ret, frame = cap.read()
    if not ret:
        break  # Exit the loop when the video ends

    # Perform object detection
    detections = model.predict(frame, threshold=0.5)

    # Mark the detected objects
    for i, box in enumerate(detections.xyxy):
        x1, y1, x2, y2 = map(int, box)
        class_id = int(detections.class_id[i])

        # Get the class name using class_id
        label = class_names.get(str(class_id), "Unknown")
        confidence = detections.confidence[i]

        # Draw the bounding box (colored and thick)
        color = (255, 255, 255)  # White color
        thickness = 7  # Thickness
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)

        # Display the label and confidence score (in white color and readable font)
        text = f"{label} ({confidence:.2f})"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        font_thickness = 7
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        text_x = x1
        text_y = y1 - 10
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 0, 255), font_thickness, cv2.LINE_AA)

    # Display the results
    resized_frame = cv2.resize(frame, (960, 540))
    cv2.imshow('Labeled Video', resized_frame)

    # Save the output
    out.write(resized_frame)

    # Exit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()  # Release the output video
cv2.destroyAllWindows()

import cv2
import requests
import time
import datetime

def draw_labels(image, detections):
    for det in detections:
        x_min, y_min, x_max, y_max = int(det['x_min']), int(det['y_min']), int(det['x_max']), int(det['y_max'])
        label = det['label']
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    return image

# Initialize webcam
cap = cv2.VideoCapture(0)

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Save the captured frame to a file
        frame_name = 'frame.jpg'
        cv2.imwrite(frame_name, frame)

        # Open the saved image file in binary mode
        with open(frame_name, 'rb') as image_file:
            files = {'image_file': image_file}
            payload = {'confidence_threshold': 0.42}
            response = requests.post('http://localhost:8000/yolov8/upload/', files=files, data=payload)

            if response.status_code == 201:
                print("Upload Successful")
                detection_result = response.json().get('detections', [])
                # Draw labels on the frame
                labeled_frame = draw_labels(frame, detection_result)
                # Save the labeled frame with a timestamp
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                cv2.imwrite(f'labeled_frame_{timestamp}.jpg', labeled_frame)
            else:
                print("Upload Failed", response.text)

finally:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

import cv2
import requests
import os
import datetime

def draw_labels(image, detections):
    for det in detections:
        x_min, y_min, x_max, y_max = int(det['x_min']), int(det['y_min']), int(det['x_max']), int(det['y_max'])
        label = det['label']
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    return image

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_name in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_name)
        image = cv2.imread(image_path)
        if image is None:
            continue

        with open(image_path, 'rb') as image_file:
            files = {'image_file': image_file}
            payload = {'confidence_threshold': 0.02}
            response = requests.post('http://localhost:8000/yolov8/upload/', files=files, data=payload)

            if response.status_code == 201:
                print(f"Upload Successful for {image_name}")
                detection_result = response.json().get('detections', [])
                labeled_image = draw_labels(image, detection_result)
                output_path = os.path.join(output_folder, f'labeled_{image_name}')
                cv2.imwrite(output_path, labeled_image)
            else:
                print(f"Upload Failed for {image_name}", response.text)

input_folder = 'example_images'
output_folder = 'example_images_output'
process_images(input_folder, output_folder)

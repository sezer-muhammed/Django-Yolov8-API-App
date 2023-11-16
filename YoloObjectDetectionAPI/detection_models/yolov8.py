from ultralytics import YOLO

class YOLOv8Detector:
    def __init__(self, model_path):
        """
        Initialize the YOLOv8 model.
        :param model_path: The path to the YOLOv8 model file (e.g., 'yolov8n.pt').
        """
        # Load the pretrained YOLOv8 model
        self.model = YOLO(model_path)

    def run_detection(self, image_path, confidence_threshold=0.42):
        """
        Run object detection on the provided image.
        :param image_path: The path to the image file.
        :return: A list of detected objects with their labels, confidence scores, and bounding boxes.
        """
        # Perform detection
        results = self.model(image_path, conf=confidence_threshold, stream=False)[0]

        # Process results
        detected_objects = []
        for det in results.boxes:  # Loop through each detection
            label_index = int(det.cls)
            label = self.model.names[label_index]
            confidence = float(det.conf)
            bbox = det.xyxy.cpu().numpy()[0]
            x_min, y_min, x_max, y_max = bbox[:4]

            detected_objects.append({
                'label': label,
                'confidence': confidence,
                'x_min': x_min,
                'y_min': y_min,
                'x_max': x_max,
                'y_max': y_max,
            })

        return detected_objects

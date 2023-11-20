# YOLOv8 Object Detection API

This project implements an object detection API using the YOLOv8 model, integrated into a Django-based web application. It allows users to upload images and run object detection, returning detected objects with labels, confidence scores, and bounding box coordinates.

Watch it here: https://youtu.be/xh0hZDpHU9o

## Features

- **Image Upload**: Users can upload images for object detection.
- **Object Detection**: Utilizes YOLOv8 for efficient and accurate object detection.
- **Admin Interface**: Django admin interface to view and manage image uploads and detections.
- **RESTful API**: Provides an API endpoint for uploading images and retrieving detection results.

## Installation

1. Clone the repository.
2. Install required dependencies:

```
pip install -r requirements.txt
```

3. Run the Django migrations:

```
python manage.py migrate
```

4. Start the Django server:

```
python manage.py runserver
```


## Usage

### Uploading Images for Detection

- Send a POST request to `/yolov8/upload/` with the image file and the desired confidence threshold.
- The API will return the detection results with labels, confidence scores, and bounding box coordinates.

### Admin Interface

- Access the Django admin interface to manage and view uploaded images and their corresponding detection results.

## API Endpoints

- `POST /upload/`: Endpoint to upload images for object detection.

## Models

- `ImageUpload`: Model to store image uploads, confidence thresholds, and status.
- `Detections`: Model to store detection results for each uploaded image.

## Admin Models

- `ImageUploadAdmin`: Admin model to manage image uploads.
- `DetectionsAdmin`: Admin model to view and manage detection results.

## Serializer

- `ImageUploadSerializer`: Serializer for image upload data.

## Views

- `UploadImageView`: API view to handle image upload requests and run object detection.

## Dependencies

- Django
- djangorestframework
- PyTorch
- Ultralytics YOLOv8

## Contributing

Contributions, issues, and feature requests are welcome!

## License

[MIT License](LICENSE)

## Acknowledgments

- Ultralytics for the YOLOv8 model.
- Django and DRF teams for the web framework and API toolkit.

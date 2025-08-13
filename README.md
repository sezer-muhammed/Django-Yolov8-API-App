# YOLOv8 Object Detection API (Django + DRF)
![Preview](https://bmeqhxsikltbwjf8.public.blob.vercel-storage.com/Screenshot%202025-08-13%20121354.png)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)](#)
[![Django](https://img.shields.io/badge/Django-4.x-092E20)](#)
[![DRF](https://img.shields.io/badge/DRF-3.x-a30000)](#)
[![YOLOv8](https://img.shields.io/badge/Ultralytics-YOLOv8-ffcc00)](https://docs.ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://img.shields.io/badge/CI-GitHub_Actions-inactive.svg)](#)

**Demo Video**
[![Watch the demo](https://img.youtube.com/vi/xh0hZDpHU9o/maxresdefault.jpg)](https://youtu.be/xh0hZDpHU9o "YOLOv8 Object Detection API Demo")


---

## Features

* **Image Upload**: Upload images for object detection.
* **Object Detection**: Uses YOLOv8 for high accuracy and efficiency.
* **Admin Interface**: Manage uploads and detections via Django Admin.
* **RESTful API**: Endpoints for uploading and retrieving detection results.

---

## Installation

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:

   ```bash
   python manage.py migrate
   ```
4. Start server:

   ```bash
   python manage.py runserver
   ```

---

## Usage

### Uploading Images

* Endpoint: `POST /yolov8/upload/`
* Params: image file + confidence threshold
* Response: Detected objects with labels, confidence scores, and bounding boxes

Example cURL:

```bash
curl -X POST http://localhost:8000/yolov8/upload/ \
  -F "image=@test.jpg" \
  -F "confidence=0.5"
```

---

## Admin Interface

* URL: `/admin/`
* Manage: Uploaded images & detection results

---

## API Endpoints

* `POST /yolov8/upload/`: Upload image & run detection

---

## Models

* **ImageUpload**: Stores image file, confidence threshold, status
* **Detections**: Stores label, score, bounding box per detection

---

## Admin Models

* **ImageUploadAdmin**: Manage image uploads
* **DetectionsAdmin**: Manage detection results

---

## Serializer

* **ImageUploadSerializer**: Handles serialization for upload data

---

## Views

* **UploadImageView**: Processes upload requests & runs YOLOv8 detection

---

## Dependencies

* Django
* djangorestframework
* PyTorch
* Ultralytics YOLOv8

---

## License

MIT License – see [LICENSE](LICENSE)

---

## Acknowledgments

* Ultralytics (YOLOv8)
* Django & DRF teams

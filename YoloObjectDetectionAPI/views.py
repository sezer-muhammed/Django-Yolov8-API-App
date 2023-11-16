from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageUpload, Detections
from .serializers import ImageUploadSerializer
from .detection_models.yolov8 import YOLOv8Detector 

class UploadImageView(APIView):
    detector = YOLOv8Detector("yolov8n.pt")

    def post(self, request, format=None):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image_upload = serializer.save()

            try:
                detection_result = self.detector.run_detection(image_path=image_upload.image_file.path, confidence_threshold=image_upload.confidence_threshold)
                image_upload.status = ImageUpload.STATUS_COMPLETED
                image_upload.save()
            except Exception as e:
                image_upload.status = ImageUpload.STATUS_FAILED
                image_upload.save()
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            for detection in detection_result:
                Detections.objects.create(
                    object_detection=image_upload,
                    label=detection['label'],
                    confidence=detection['confidence'],
                    x_min=detection['x_min'],
                    x_max=detection['x_max'],
                    y_min=detection['y_min'],
                    y_max=detection['y_max']
                )

            return Response({'detections': detection_result}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

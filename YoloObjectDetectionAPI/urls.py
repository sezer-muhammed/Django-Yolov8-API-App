from django.urls import path
from .views import UploadImageView

urlpatterns = [
    path('upload/', UploadImageView.as_view(), name='upload-image'),
]

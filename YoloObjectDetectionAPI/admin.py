from django.contrib import admin
from .models import ImageUpload, Detections
from django.utils.html import format_html

@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'image_file', 'upload_timestamp', 'confidence_threshold', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'upload_timestamp')
    search_fields = ('image_file', 'status')

    def thumbnail(self, obj):
        if obj.image_file:
            return format_html('<img src="{}" style="width: 250px; height:auto;"/>', obj.image_file.url)
        return "-"
    thumbnail.short_description = "Thumbnail"


@admin.register(Detections)
class DetectionsAdmin(admin.ModelAdmin):
    list_display = ('object_detection', 'label', 'confidence', 'x_min', 'x_max', 'y_min', 'y_max', 'detection_date')
    list_filter = ('object_detection', 'label', 'detection_date')
    search_fields = ('label', 'object_detection__linked_image__image_file')

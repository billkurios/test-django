from django.urls import path

from .views.file_upload import FileUploadUDView, FileUploadCRView


urlpatterns = [
    path("upload-file/", FileUploadCRView.as_view()),
    path("upload-file/<int:item_id>", FileUploadUDView.as_view()),
]

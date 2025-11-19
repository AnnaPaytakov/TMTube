from django.urls import path
from .views import VideosListView,UploadVideoView,VideoDetailView

urlpatterns = [
    path("", VideosListView.as_view(), name="videos"),
    path("upload/", UploadVideoView.as_view(), name="upload_video"),
    path("video/<int:pk>/", VideoDetailView.as_view(), name="video"),
]
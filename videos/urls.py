from django.urls import path
from . import views

urlpatterns = [
    path("", views.videos, name="videos"),
    path("upload/", views.upload_video, name="upload_video"),
    path("video/<str:pk>/", views.video, name="video"),
]

import os
from django.conf import settings
from django.views.generic import FormView, ListView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import VideoForm
from .models import Video


class UploadVideoView(FormView):
    template_name = "videos/upload.html"
    form_class = VideoForm
    success_url = reverse_lazy("videos")

    def form_valid(self, form):
        try:
            video = form.save()

            print(f"Имя файла: {video.file.name}")
            print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")

            file_path = os.path.join(settings.MEDIA_ROOT, video.file.name)

            print(f"Сформированный путь: {file_path}")
            print(f"Существование файла: {os.path.exists(file_path)}")

            if not os.path.exists(file_path):
                print(f"Файл не найден: {file_path}")
                form.add_error(None, "Файл не найден")
                return self.form_invalid(form)

            Video.convert_to_hls(video)
            return super().form_valid(form)

        except Exception as e:
            print(f"Полная ошибка: {e}")
            form.add_error(None, str(e))
            return self.form_invalid(form)
        
#* List Videos
class VideosListView(ListView):
    model = Video
    template_name = "videos/videos.html"
    context_object_name = "videos"
    ordering = ["-uploaded_at"]

#* Single Video
class VideoDetailView(DetailView):
    model = Video
    template_name = "videos/video.html"
    context_object_name = "video"
    pk_url_kwarg = "pk"
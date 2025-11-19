import os
from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
from django.conf import settings

#! CBV gecmeli
def upload_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
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
                    return render(request, "videos/upload.html", {"form": form})

                Video.convert_to_hls(video)
                return redirect("videos")
            except Exception as e:
                print(f"Полная ошибка: {e}")
                form.add_error(None, str(e))
    else:
        form = VideoForm()
    return render(request, "videos/upload.html", {"form": form})

#! CBV gecmeli
def videos(request):
    videos = Video.objects.all().order_by("-uploaded_at")
    context = {
        "videos": videos,
    }
    return render(request, "videos/videos.html", context)

#! CBV gecmeli
def video(request, pk):
    video = Video.objects.get(id=pk)
    context = {
        "video": video,
    }
    return render(request, "videos/video.html", context)
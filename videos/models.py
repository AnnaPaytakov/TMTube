from django.db import models
import os
import subprocess
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Video(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    file = models.FileField(upload_to="videos/", verbose_name="Файл видео")
    hls_playlist = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="HLS Плейлист"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return self.title

    #! boleklere bolyar
    @classmethod
    def convert_to_hls(cls, instance):
        if not instance.file:
            return

        input_path = instance.file.path

        hls_folder = os.path.join(settings.MEDIA_ROOT, "hls", f"hls_{instance.id}")
        os.makedirs(hls_folder, exist_ok=True)

        hls_path = os.path.join(hls_folder, "output.m3u8")

        cmd = [
            settings.FFMPEG_PATH,
            "-i",
            input_path,
            "-profile:v",
            "baseline",
            "-level",
            "3.0",
            "-preset",
            "fast",
            "-start_number",
            "0",
            "-hls_time",
            "10",
            "-hls_list_size",
            "0",
            "-f",
            "hls",
            hls_path,
        ]

        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8",
                text=True,
            )

            if result.returncode != 0:
                print(f"Ошибка FFmpeg: {result.stderr}")
                return

            instance.hls_playlist = os.path.relpath(hls_path, settings.MEDIA_ROOT)
            instance.save()
        except Exception as e:
            print(f"Ошибка конвертации: {e}")


@receiver(post_save, sender=Video)
def convert_video_to_hls(sender, instance, created, **kwargs):
    if created:
        instance.convert_to_hls(instance)

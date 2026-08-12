# 🎬 TMTube

A personal project aimed at building a YouTube-like video platform for Turkmenistan.

The project focuses on video uploading, server-side video processing with FFmpeg, and HTTP Live Streaming (HLS) for delivering processed video content.

## ✨ Features

- 🎥 Video upload
- 📝 Video title and description
- 📺 Video listing and detail pages
- ⚙️ Server-side video processing with FFmpeg
- 📡 HLS (HTTP Live Streaming) video delivery
- 🧩 Automatic generation of `.m3u8` playlists and HLS segments
- 👤 Basic user application structure

## 🛠️ Tech Stack

- Python
- Django
- FFmpeg
- HLS (HTTP Live Streaming)
- UV

## ⚙️ How It Works

When a video is uploaded, the application stores the original file and processes it with FFmpeg.

The video is converted into HLS format, producing:

- an `.m3u8` playlist
- segmented video files

The generated HLS playlist is then associated with the uploaded video and can be used for streaming.

```text
Video Upload
     │
     ▼
Django
     │
     ▼
FFmpeg Processing
     │
     ▼
HLS Conversion
     │
     ├── output.m3u8
     └── video segments
             │
             ▼
        HLS Playback
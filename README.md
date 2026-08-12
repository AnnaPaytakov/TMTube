# TMTube

A personal project aimed at building a YouTube-like video platform for Turkmenistan.

The project focuses on video uploading, server-side video processing with FFmpeg, and HTTP Live Streaming (HLS) for delivering processed video content.

## Features

-  Video upload
-  Video title and description
-  Video listing and detail pages
-  Server-side video processing with FFmpeg
-  HLS (HTTP Live Streaming) video delivery
-  Automatic generation of `.m3u8` playlists and HLS segments
-  Basic user application structure

## Tech Stack

- Python
- Django
- FFmpeg
- HLS
- UV

## How It Works


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
```text

## Future Improvements

- Background video processing with Celery
- Redis-based task queue for asynchronous video processing
- Adaptive bitrate streaming with multiple video resolutions
- Optimized video delivery and caching


## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.10+
- FFmpeg
- UV

### FFmpeg

FFmpeg is required for video processing and HLS conversion.

After installing FFmpeg, make sure it is available in your system `PATH` or configure its executable path in the Django settings.

You can verify the installation with:

```bash
ffmpeg -version
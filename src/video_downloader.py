from yt_dlp import YoutubeDL
import os


def download_video(url):
    ydl_opts = {
        "format": "bestvideo[ext=mp4][vcodec!=av01]+bestaudio[ext=m4a]/best[ext=mp4]",
        "outtmpl": os.path.join("temp", "%(id)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "ExecAfterDownload",
                "exec_cmd": "ffmpeg -y -i {} -c:v libx264 -preset fast {}.temp.mp4 && mv {}.temp.mp4 {}",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

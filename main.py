import sys
import re
from time import sleep
from yt_dlp import YoutubeDL as ytmd

def main():
    if len(sys.argv) < 2:
        print('USAGE: main.py "<URL>" "<OUTPUT OPTIONS>"')
        sys.exit(1)

    url = sys.argv[1]
    if not re.search("youtube.com", url):
        print("Input is not a YT link.")
        sys.exit(1)

    out_opt = sys.argv[2] if len(sys.argv) > 2 else None

    ydl_opts = {
        "format": "mp3/bestaudio/best",
        "writethumbnail": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3"
            },
            {
                "key": "FFmpegMetadata",
                "add_chapters": True,
                "add_infojson": "if_exists",
                "add_metadata": True
            },
            {
                "key": "EmbedThumbnail",
                "already_have_thumbnail": False
            }
        ],
    }

    if out_opt:
        print("Using custom output options...")
        sleep(1)
        ydl_opts["outtmpl"] = f"./out/{out_opt}"
    else:
        print("Using default output options...")
        sleep(1)
        ydl_opts["outtmpl"] = "./out/%(creator)s - %(title)s.%(ext)s"

    with ytmd(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    main()
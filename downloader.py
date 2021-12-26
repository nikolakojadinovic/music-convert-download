import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with open('links.txt', 'r') as yt_link:
    links = yt_link.readlines()

for line in links:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([line])
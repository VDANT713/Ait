import urllib.request
import re

urls = [
    "https://youtu.be/wfhILwzjDPM",
    "https://youtu.be/5E6wtIc4zHk",
    "https://youtu.be/5L-g16Aok_Y",
    "https://youtu.be/PCB8eED9fKA",
    "https://youtu.be/ok_CoAmKNow",
    "https://youtu.be/uZz3bMKk9ZY",
    "https://youtu.be/yT5qkwMuy7U",
    "https://youtu.be/Gzds8mtgF6w",
    "https://youtu.be/gdAlKRM6tbM",
    "https://youtu.be/0vK2dU-9Nik"
]

for i, url in enumerate(urls):
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8')
        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        title = title_match.group(1).replace(" - YouTube", "") if title_match else "Unknown"
        video_id = url.split('/')[-1]
        print(f'{i+1}. ID: {video_id} | Title: {title}')
    except Exception as e:
        print(f'{i+1}. URL: {url} | Error: {e}')

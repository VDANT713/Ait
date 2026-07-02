import urllib.request
import re

video_ids = [
    "gucD6ESzkFU",
    "ZW1wWuT_dog",
    "LU3K5mBeUyA",
    "ehG2ylJx4zc",
    "z9aNgZ5-Zxg"
]

for vid in video_ids:
    url = f"https://www.youtube.com/watch?v={vid}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        title_match = re.search(r'<title>(.*?)</title>', html)
        title = title_match.group(1).replace(" - YouTube", "") if title_match else "Unknown Title"
        print(f"{vid} | {title}")
    except Exception as e:
        print(f"Failed to fetch {vid}: {e}")

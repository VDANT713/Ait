import urllib.request
import re

video_ids = [
    "HIb0hTiyJIs",
    "CYYp1CUdvjE",
    "CyNoiX3rA4w",
    "PuC1TeSYiIw",
    "KCrhP5lXaQs"
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

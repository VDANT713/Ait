import re

with open("podcast_segment.html", "r") as f:
    podcast_html = f.read()

with open("index.html", "r") as f:
    content = f.read()

# The section starts with <!-- Podcasts --> and ends with </section> before <!-- Behind The Work -->
start_str = "<!-- Podcasts -->"
end_str = "<!-- Behind The Work -->"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + podcast_html + "\n        " + content[end_idx:]
    with open("index.html", "w") as f:
        f.write(new_content)
    print("Successfully replaced podcast segment in index.html")
else:
    print("Could not find start or end markers")

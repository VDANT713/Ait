import html

videos = [
    ("wfhILwzjDPM", "Inside the Legal Fight for Ram Mandir | Harishankar Jain Shares Courtroom Stories | Changemakers"),
    ("5E6wtIc4zHk", "History of Guru Shishya Parampara | Prof. Ram Nath Jha | Prachyam TV |"),
    ("5L-g16Aok_Y", "Dating Ramayan & Mahabharat | Dwarka Submerge Under Sea?| Secrets of Astronomy with Nilesh Oak"),
    ("PCB8eED9fKA", "Randeep Hooda Full Podcast | Swatantrya Veer Savarkar Movie | Life and Controversies around Savarkar"),
    ("ok_CoAmKNow", "Koenraad Elst On Ram Mandir, Gyanvapi, Nupur Sharma & Fact Checking Business | Secularism in India"),
    ("uZz3bMKk9ZY", "Most Dangerous Enemies of Hindus? | Ram Mandir, Kashi Vishwanath | Adv. Hari Shankar Jain"),
    ("yT5qkwMuy7U", "Babur Did Not Construct Babri Masjid? | Life & Times of Babur | Aabhas Maldahiyar Interview"),
    ("Gzds8mtgF6w", "Official Trailer | Savarkar: Visionary or Traitor? | Exposing the Leftist Agenda | Uday Mahurkar"),
    ("gdAlKRM6tbM", "Official Trailer | G.B.Deglurkar Teaches Temple Architecture | Indiclass | Prachyam TV"),
    ("0vK2dU-9Nik", "How did British Destroy Indian Guru Shishya Parampara? | Pt. Satish Sharma")
]

pages = [
    videos[0:6],
    videos[6:10]
]

output = """        <!-- Podcasts -->
        <section class="content-section" id="podcasts">
            <div class="container">
                <h2 class="section-title" style="margin-bottom: 2rem;">Podcasts</h2>
            </div>
            
            <div class="slider-container" id="podcast-container" style="display: flex; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; scroll-behavior: smooth; width: 100%;">
"""

for page in pages:
    output += '                <!-- PAGE -->\n'
    output += '                <div class="slider-page grid projects-grid" style="width: 100%; flex-shrink: 0; padding: 0 2rem; scroll-snap-align: start;">\n'
    for video_id, title in page:
        safe_title = html.escape(title)
        output += f"""                    <a href="https://youtu.be/{video_id}" target="_blank" class="card video-card">
                        <div class="card-img-wrapper">
                            <img src="https://img.youtube.com/vi/{video_id}/maxresdefault.jpg" alt="{safe_title}">
                        </div>
                        <div class="card-content">
                            <h3>{safe_title}</h3>
                            <p class="subtitle">AIT INDIA</p>
                        </div>
                    </a>\n"""
    output += '                </div>\n'

output += '            </div>\n'
output += '            <div class="pagination-controls pill-pagination">\n'
for i in range(len(pages)):
    active_class = " active-page-btn" if i == 0 else ""
    output += f'                <button class="pill-page-btn{active_class} podcast-page-num" data-page="{i}">{i+1}</button>\n'
output += '            </div>\n'
output += '        </section>'

with open("podcast_segment.html", "w") as f:
    f.write(output)

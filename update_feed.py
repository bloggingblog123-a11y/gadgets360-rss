import feedparser
from xml.sax.saxutils import escape

SOURCE_FEED = "https://www.gadgets360.com/rss/feeds"

feed = feedparser.parse(SOURCE_FEED)

items = []

for entry in feed.entries:
    title = escape(entry.get("title", "Gadgets 360"))
    link = escape(entry.get("link", ""))
    guid = escape(entry.get("id", link))
    description = escape(
        entry.get("summary", entry.get("description", ""))
    )
    published = escape(entry.get("published", ""))

    items.append(f"""
    <item>
      <title>{title}</title>
      <link>{link}</link>
      <guid isPermaLink="false">{guid}</guid>
      <description>{description}</description>
      <pubDate>{published}</pubDate>
    </item>
    """)

xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Gadgets 360 - All Stories</title>
    <link>https://www.gadgets360.com/</link>
    <description>Latest stories from Gadgets 360</description>
    <language>en-IN</language>
    <generator>Personal Gadgets 360 RSS Feed</generator>
    {''.join(items)}
  </channel>
</rss>
"""

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print(f"Created feed.xml with {len(items)} stories")

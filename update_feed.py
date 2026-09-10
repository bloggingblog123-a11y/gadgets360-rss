import feedparser
from xml.etree.ElementTree import Element, SubElement, ElementTree

SOURCE_FEED = "https://www.gadgets360.com/rss"
OUTPUT_FILE = "feed.xml"

feed = feedparser.parse(SOURCE_FEED)

rss = Element("rss", {"version": "2.0"})
channel = SubElement(rss, "channel")

SubElement(channel, "title").text = "Gadgets 360 - All Stories"
SubElement(channel, "link").text = "https://www.gadgets360.com/"
SubElement(channel, "description").text = (
    "Latest stories from Gadgets 360. "
    "Source: Gadgets 360."
)

for item in feed.entries:
    entry = SubElement(channel, "item")

    SubElement(entry, "title").text = item.get("title", "")
    SubElement(entry, "link").text = item.get("link", "")
    SubElement(entry, "guid").text = item.get("id", item.get("link", ""))

    if item.get("summary"):
        SubElement(entry, "description").text = item.summary

    if item.get("published"):
        SubElement(entry, "pubDate").text = item.published

tree = ElementTree(rss)
tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)

print(f"Updated RSS feed with {len(feed.entries)} stories.")

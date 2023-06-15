import shutil
from datetime import datetime
from feedgen.feed import FeedGenerator
import pytz
import os

# Define the hard drive names and their corresponding paths
hard_drives = {"Burger": "/", "Sandwich": "/Volumes/Sandwich 1", "Donuts": "/Volumes/Donuts"}

# Create the RSS feed
fg = FeedGenerator()
fg.title("Hard Drive Space")
fg.link(href="http://example.com", rel="alternate")
fg.description("Percentage of Used Space for Hard Drives")
fg.language("en")

# Get the percentage of used space for each hard drive
for drive, path in hard_drives.items():
    if not os.path.exists(path):
        continue
    
    total, used, free = shutil.disk_usage(path)
    percentage_used = (used / total) * 100

    # Create an RSS item for each hard drive
    fe = fg.add_entry()
    fe.title(f"{drive} Usage")
    fe.link(href="http://example.com/drive-usage")
    fe.description(f"{drive}: {percentage_used:.2f}% used")
    fe.pubDate(datetime.now(pytz.timezone('America/Sao_Paulo')))

# Save the RSS feed to a file
fg.rss_file("hds.rss")

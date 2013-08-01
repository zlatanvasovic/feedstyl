#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Python feed parser
#

import sys
import feedparser

# Set up
# ------

# List of uples (label, property-tag, truncation)
COMMON_CHANNEL_PROPERTIES = [
  ("Channel title:", "title", None),
  ("Channel description:", "description", 100),
  ("Channel URL:", "link", None),
]

COMMON_ITEM_PROPERTIES = [
  ("Item title:", "title", None),
  ("Item description:", "description", 50),
  ("Item URL:", "link", None),
]

INDENT = u" "*2

# Data
# ----

def feedinfo(url, output=sys.stdout):
  # Read an RSS or Atom feed from the given URL and output a feed report with
  # all the key data
  feed_data = feedparser.parse(url)
  channel, items = feed_data.feed, feed_data.entries

  # Display channel data
  for label, prop, trunc in COMMON_CHANNEL_PROPERTIES:
    value = channel[prop]
    if trunc:
      value = value[:trunc] + u"..."
    print >> output, label, value

  # Display item data
  print >> output, "\nFeed items:\n"
  for item in items:
    for label, prop, trunc in COMMON_ITEM_PROPERTIES:
      print >> output, INDENT, u"---"
      value = item[prop]
      if trunc:
        value = value[:trunc] + u"..."
      print >> output, INDENT, label, value
      print >> output, INDENT, u"---\n"
  return

# Parse feed
# ----------

if __name__ == "__main__":
  url = sys.argv[1]
  feedinfo(url)

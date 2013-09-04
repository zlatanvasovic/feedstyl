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
feed_properties = [
  ("\n\033[1mFeed title:\033[0m", "title", None),
  ("\033[1mFeed description:\033[0m", "description", 57),
  ("\033[1mFeed URL:\033[0m", "link", None),
]

item_properties = [
  ("\033[1mItem title:\033[0m", "title", None),
  ("\033[1mItem description:\033[0m", "description", 55),
  ("\033[1mItem URL:\033[0m", "link", None),
]

indent = " "

# Data
# ----

def feedinfo():
  # Get feed and item data
  output = sys.stdout
  data = feedparser.parse(sys.argv[1])

  # Display feed data
  for label, prop, trunc in feed_properties:
    value = data.feed[prop]
    if trunc:
      value = value[:trunc] + "..."
    print >> output, label, value

  # Display item data
  print >> output, "\n\033[1mFeed items:\033[0m\n"
  for item in data.entries:
    for label, prop, trunc in item_properties:
      value = item[prop]
      if trunc:
        value = value[:trunc] + "..."
      print >> output, indent, label, value
    print ""
  return

# Parse feed
# ----------

if __name__ == "__main__":
  feedinfo()
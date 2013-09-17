#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Python feed parser
#

import sys
import feedparser

# Set up
# ------

# Data for parse
data = feedparser.parse(sys.argv[1])

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

# Parse feed
# ----------

if __name__ == "__main__":
  # Display feed data
  for label, prop, trunc in feed_properties:
    value = data.feed[prop]
    if trunc:
      value = value[:trunc] + "..."
    print >> sys.stdout, label, value

  # Display item data
  print >> sys.stdout, "\n\033[1mFeed items:\033[0m\n"
  for item in data.entries:
    for label, prop, trunc in item_properties:
      value = item[prop]
      if trunc:
        value = value[:trunc] + "..."
      print >> sys.stdout, " ", label, value
    print ""
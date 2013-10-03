#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Python script for displaying pretty RSS feeds
#

import sys
import feedparser

# List of uples (label, property tag, truncation)
# -----------------------------------------------

feed_properties = [
  ("\n\033[1mFeed title:\033[0m", "title", None),
  ("\033[1mFeed description:\033[0m", "description", 59),
  ("\033[1mFeed URL:\033[0m", "link", None),
]

item_properties = [
  ("\033[1mItem title:\033[0m", "title", None),
  ("\033[1mItem description:\033[0m", "description", 55),
  ("\033[1mItem URL:\033[0m", "link", None),
]

# Parse feed
# ----------

# Display core feed properties
for label, prop, trunc in feed_properties:
  value = feedparser.parse(sys.argv[1]).feed[prop]
  if trunc is not None and len(value) >= trunc:
    value = value[:trunc] + "..."
  print >> sys.stdout, label, value

# Display core item properties
print >> sys.stdout, "\n\033[1mFeed items:\033[0m\n"
for item in feedparser.parse(sys.argv[1]).entries:
  for label, prop, trunc in item_properties:
    value = item[prop]
    if trunc:
      value = value[:trunc] + "..."
    print >> sys.stdout, " ", label, value
  print ""
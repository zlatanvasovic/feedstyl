#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Script for displaying pretty RSS feeds
#

from sys import argv
import feedparser

# Data for parsing
data = feedparser.parse(argv[1])

# Display core feed properties
print "\n\033[1mFeed title:\033[0m", data.feed.title
if "description" in data.feed:
  if len(data.feed.description) > 59:
    data.feed.description = data.feed.description[:59] + "..."
  print "\033[1mFeed description:\033[0m", data.feed.description
print "\033[1mFeed link:\033[0m", data.feed.link

# Display core items properties
print "\n\033[1mFeed entries:\033[0m\n"
for entry in data.entries:
  print "  \033[1mEntry title:\033[0m", entry.title
  if "description" in entry:
    if len(entry.description) > 54:
      entry.description = entry.description[:54] + "..."
    print "  \033[1mEntry description:\033[0m", entry.description
  print "  \033[1mEntry link:\033[0m", entry.link, "\n"
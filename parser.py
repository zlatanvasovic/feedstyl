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
print "\033[1mFeed URL:\033[0m", data.feed.link

# Display core items properties
print "\n\033[1mFeed entries:\033[0m\n"
for item in data.entries:
  print "  \033[1mEntry title:\033[0m", item.title
  if "description" in item:
    if len(item.description) > 54:
      item.description = item.description[:54] + "..."
    print "  \033[1mEntry description:\033[0m", item.description
  print "  \033[1mEntry URL:\033[0m", item.link, "\n"
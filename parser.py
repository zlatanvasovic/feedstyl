#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Script for displaying pretty RSS feeds
#

from sys import argv
import feedparser

# Feed data for parse
data = feedparser.parse(argv[1])

# Display core feed data
print "\n\033[1mFeed title:\033[0m", data.feed.title
if "description" in data.feed:
  feed_d = data.feed.description
  if len(feed_d) > 59:
    feed_d = feed_d[:59] + "..."
  print "\033[1mFeed description:\033[0m", feed_d
print "\033[1mFeed URL:\033[0m", data.feed.link

# Display core items data
print "\n\033[1mFeed items:\033[0m\n"
for item in data.entries:
  print "  \033[1mItem title:\033[0m", item.title
  if "description" in item:
    item_d = item.description
    if len(item_d) > 55:
      item_d = item_d[:55] + "..."
    print "  \033[1mItem description:\033[0m", item_d
  print "  \033[1mItem link:\033[0m", item.link, "\n"
#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Script for displaying pretty feeds
#

from sys import argv
import feedparser

# Error handlers
# --------------

# Check for incorrect usage
if len(argv) == 1:
  print "URL is missing.\n"
  url = raw_input("Enter it: ")
# Default case
else:
  url = argv[1]

# Fix weird links without `http`
if not (url.startswith("http://") or url.startswith("https://")):
  url = "http://" + url

# Configuration
# -------------

# Indent
indent_lenght = 2
indent = " " * indent_lenght

# Truncation (depends on indent)
feed_trunc = 59
entry_trunc = 56

# Functions
# ---------

# Bold decoration
def bold(string):
  return "\033[1m" + string + "\033[0m"

# Truncation
def trunc(trunc, string):
  if len(string) > trunc:
    string = string[:trunc] + "..."
  return string

# Display data
# ------------

# Feed data
data = feedparser.parse(url)

# Display core feed properties
print bold("\nFeed title: ") + data.feed.title
if "description" in data.feed:
  print bold("Feed description: ") + trunc(feed_trunc, data.feed.description)
print bold("Feed link: ") + data.feed.link

# Display core items properties
print bold("\nFeed entries:\n")
for entry in data.entries:
  print indent + bold("Entry title: ") + entry.title
  if "description" in entry:
    print indent + bold("Entry description: ") + \
    trunc(entry_trunc, entry.description)
  print indent + bold("Entry link: ") + entry.link + "\n"
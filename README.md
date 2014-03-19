# Feedstyl

> Script for displaying stylish feeds

Feedstyl is a script for displaying stylish, minimalistic feeds.

For more info about content parsing, read
[sanitization article](http://pythonhosted.org/feedparser/html-sanitization.html)
at feedparser documentation.

## Dependencies

- Python 3
- [feedparser](http://code.google.com/p/feedparser/)

## Command line

```bash
$ ./feedstyl.py URL
```

You can alias is to `feedstyl` or something similarly if you want nicer usage.

## API

Feedstyl is meant to be used only in the command line as **distinct command**.
However, you can import Feedstyl in the another script. You have to import it
locally.

```py
import feedstyl
```

### .feed()

**Usage:** `feedparser.feed()`

Displays feed properties.

### .entries()

**Usage:** `feedparser.entries()`

Displays entries properties.

### .main()

**Usage:** `feedparser.main()`

Displays both feed and entries properties.

## Configuration

Configuration values:

- `indent_lenght` (used for calculating `indent`)
- `feed_trunc`
- `entry_trunc`

## License

MIT &copy; [Zlatan Vasović](https://github.com/ZDroid)

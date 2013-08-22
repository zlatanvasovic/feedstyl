# parser.py

**parser.py** is Python script for parsing RSS and Atom feeds. Based on [one of IBM developerWorks](http://www.ibm.com/developerworks/xml/library/x-tipufp/).

Licensed under the terms of MIT license.

## Usage

Run:
```bash
$ ./parser.py $feed
```

Replace `$feed` with your wanted feed.

## Notes

* Requires [feedparser](http://code.google.com/p/feedparser/) module.
* Some Atom feeds cannot be parsed (feedparser bug).

## Author

**Zlatan Vasović**
* https://twitter.com/zdr0id
* https://github.com/ZDroid

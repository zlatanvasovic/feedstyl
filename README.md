# What is PyRSS?

**PyRSS** (<b>PythonRSS</b>) is script for parsing RSS feeds and `python terminal` run.

Its name isn't factor for usage, It works with RSS, Atom and XML feeds.

**PyRSS site** is created with github pages. PyRSS site (`gh-pages` branch) → http://zdroid.github.com/PyRSS/.

# How to help me with testing?

If you interested in testing PyRSS, contact me on **zdroid@zdroidblog.info**.

# Notes

You need **`feedparser` python module** for normal work of this script.

<b>feedparser</b> → http://code.google.com/p/feedparser/

# Cloning

```shell
$ git clone git://github.com/ZDroid/PyRSS
```

# Simple run

```shell
$ python /path/to/PyRSS/rss.py http://link.to.rss-feed.com/rss-feed
```
Replace `http://link.to.rss.feed/rss-feed` with your wanted (RSS/Atom/XML) feed.

# Example output
```shell
Channel title: Zlatan Vasović
Channel description: Blog o slobodnom softveru...
Channel URL: http://zdroidblog.info

Feed items:
     Item title: Izmene…
     Item description: Nažalost, dva Week feed-a su preskočena zbog izmena&#8230; Šta je novo: WordPress.org i WordPress te...
     Item URL: http://zdroidblog.info/?p=186
     ---
     Item title: Week feed 2
     Item description: Week feed je dogurao do 2. izdanja&#8230; uživajte! 29. novembar Screenshot aplikacija Screencloud j...
     Item URL: http://zdroidblog.info/?p=112
     ---
     Item title: Week feed 1
     Item description: Odlučio sam da od sada dodajem i nedeljni pregled svih vesti o slobodnom softveru koji sam nazvao „W...
     Item URL: http://zdroidblog.info/?p=72
     ---
     Item title: Terminal (konzola) – stanje sistema
     Item description: Zanima Vas stanje procesora, memorije, zauzeće HDD-a i sl? Onda koristiti komande za stanje sistema....
     Item URL: http://zdroidblog.info/?p=43
     ---
     Item title: ZAW ikonice
     Item description: U pripremi su ZAW ikonice koje bi bile unapređena verzija Faenza-e kombinovanjem više stilova (Faenz...
     Item URL: http://zdroidblog.info/?p=36
     ---
     Item title: Dobrodošli!
     Item description: Dobrodošli na moj novi blog! Stari i dalje možete naći na adresi www.zdroidblog.info (sa www uvek, n...
     Item URL: http://zdroidblog.info/?p=7
     ---
```

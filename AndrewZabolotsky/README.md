# RSS reader

## Usage

```
$ python -m rss_reader --help
usage: rss_reader [-h] [--source SOURCE] [--to-html PATH] [--to-fb2 PATH] [--version] [--json] [--colorize] [--verbose] [--limit LIMIT] [--date DATE]

Pure Python command-line RSS reader.

optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  RSS URL
  --to-html PATH   Outputs news to file in HTML format
  --to-fb2 PATH    Outputs news to file in FB2 format
  --version        show program's version number and exit
  --json           Print result as JSON in stdout
  --colorize       Colorize output
  --verbose        Outputs verbose status messages
  --limit LIMIT    Limit news topics if this parameter provided
  --date DATE      Defines date news for catching
```

Feching news from `https://news.yahoo.com/rss/`:
```
$ python -m rss_reader --source https://news.yahoo.com/rss/ --limit 2 2>/dev/null 

		Title: Yahoo News - Latest News & Headlines
		Link: https://www.yahoo.com/news

Title: Asian spider takes hold in Georgia, sends humans scurrying
Date: 2021-10-29 13:43:21
Link: https://news.yahoo.com/asian-spider-takes-hold-georgia-134321868.html

Title: Tyler Perry says he suggested 'Survivor' make swimsuits 'look worn and tattered' but denies telling Jeff Probst to get rid of them altogether
Date: 2021-10-30 01:11:57
Link: https://news.yahoo.com/tyler-perry-says-suggested-survivor-011157169.html
```

### --json
Outputs each feed in JSON format.

Example:
```json
[
    {
        "Title": "Yahoo News - Latest News & Headlines",
        "Link": "https://www.yahoo.com/news",
        "Image": "http://l.yimg.com/rz/d/yahoo_news_en-US_s_f_p_168x21_news.png",
        "Articles": [
            {
                "Title": "Asian spider takes hold in Georgia, sends humans scurrying",
                "Date": "2021-10-29 13:43:21",
                "Link": "https://news.yahoo.com/asian-spider-takes-hold-georgia-134321868.html"
            }
        ]
    }
]
```
### News caching

If `--date` is passed, then news are always fetched from cache. 
If `--source` is passed together with `--date`, then news are fetched from cache only for specified source. 
Fresh news are fetched when only `--source` is passed without `--date`.

Under the hood cache is implemented as directory which contins a file per source.

## Installation

```bash
python3 -m pip install --extra-index-url https://test.pypi.org/simple/ rss-reader-by-andrew-zabolotsky
```

## Contributing
### How to run tests

```bash
python3 -m unittest discover -s tests
```

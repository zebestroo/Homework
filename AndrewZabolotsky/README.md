# RSS reader
## --json
Prints each article in separete line. Lines expressed in JSON format.


Example:
```json
	{
		"Title": "Now 41, man who killed 4-year-old at age 13 granted parole", # Article's title
		"Date": "2021-10-16 14:32:42", # Article's date of publishing
		"Link": "https://news.yahoo.com/now-41-killer-4-old-143242635.html" # Link to article
	}
```

## Installation

```bash
python3 -m pip install --extra-index-url https://test.pypi.org/simple/ rss-reader-by-andrew-zabolotsky
```
## Contributing
### How to run tests

```bash
python3 -m unittest discover -s tests
```

## News caching

If `--date` is passed, then news are always fetched from cache. 
If `--source` is passed together with `--date`, then news are fetched from cache only for specified source. 
Fresh news are fetched when only `--source` is passed without `--date`

Under the hood cache is implemented as directory which contins a file per source.

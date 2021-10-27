"""
Utils for working with cache.
"""
import hashlib
import logging
import json
import os
from datetime import datetime
from .rss_reader import Article, Feed


class Cache:
    """
    Provides possibilities to cache feeds. Under the hood a directory with files.
    Each file represents separate source.
    """

    def __init__(self, dir_name=".cached"):
        """
        Creates directory for cache if needed
        """
        self.cached_dir = dir_name
        if not os.path.exists(self.cached_dir):
            logging.debug(f"Creating {self.cached_dir} cache directory")
            os.mkdir(self.cached_dir)

    def _source_to_path(self, source):
        """
        Creates path to file in self.dir_name directory made with source(url)
        """
        fname = hashlib.md5(source.encode()).hexdigest()
        return os.path.join(self.cached_dir, fname)

    def _list_of_paths(self):
        """
        Returns list of filenames in self.dir_name 
        """
        return [os.path.join(self.cached_dir, name) for name in os.listdir(self.cached_dir)]

    def _feed_from_dict(self, obj):
        """
        Construct Feed from dict
        """
        feed = Feed(articles=[], title=obj["Title"], link=obj["Link"], image=obj["Image"])
        for item in obj["Articles"]:
            feed.articles.append(self._article_from_dict(item))
        return feed

    def _feed_to_dict(self, feed):
        """
        Inverse function to _feed_from_dict
        """
        obj = {"Title": feed.title, "Link": feed.link, "Image": feed.image}
        ls = []
        for article in feed.articles:
            ls.append(self._article_to_dict(article))
        obj["Articles"] = ls
        return obj

    def _article_from_dict(self, item):
        """
        Construct article from inner storage dict
        """
        return Article(item["Title"], item["Link"], datetime.fromisoformat(item["Date"]))

    def _article_to_dict(self, article):
        """
        Construct inner storage dict from article
        """
        return {
            "Title": article.title,
            "Date": article.date.isoformat(),
            "Link": article.link
        }

    def store(self, source, feed):
        """
        Writes feed in file by source
        """
        with open(self._source_to_path(source), 'w') as file:
            logging.debug(f"Updating {source} in cache")
            json.dump(self._feed_to_dict(feed), file)

    def load(self, source=None, date=None, limit=None):
        """
        Loads feeds from all sources
        """
        result = []
        paths = [self._source_to_path(source)] if source else self._list_of_paths()
        for path in paths:
            feed = self._load_by_path(path)
            if not feed:
                continue
            if date:
                total = len(feed.articles)
                feed.articles = list(filter(lambda pub: pub.date.date() == date, feed.articles))
                logging.debug(f"Selected {len(feed.articles)} from {total} by {date}")
            feed.articles = feed.articles[:limit]
            if feed.articles:
                result.append(feed)
            if limit:
                limit -= len(feed.articles)
                if limit == 0:
                    logging.debug(f"Reached limit by articles count")
                    break
        return result

    def _load_by_path(self, path):
        """
        Loads feed from file by path
        """
        if not os.path.exists(path):
            logging.warning(f"Trying load feed by non-exist path {path}")
            return None
        with open(path, 'r') as file:
            logging.debug(f"Loading feed from path {path}")
            return self._feed_from_dict(json.load(file))

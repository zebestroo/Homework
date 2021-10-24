"""
Utils for working with cache.
"""
import json
import os
from datetime import datetime
from urllib.parse import urlparse
from .rss_reader import Article


class Cache:
    """
    Provides possibilities to cache articles from different sources. Under the hood a directory with files.
    Each file represents separate source.
    """

    def __init__(self, dir_name=".cached"):
        self.cached_dir = dir_name
        if not os.path.exists(self.cached_dir):
            os.mkdir(self.cached_dir)

    def source_to_path(self, source):
        """
        Creates path to file in self.dir_name directory made with source(url)
        """
        return os.path.join(self.cached_dir, urlparse(source).hostname)

    def list_of_paths(self):
        """
        Returns list of filenames in self.dir_name 
        """
        return [os.path.join(self.cached_dir, name) for name in os.listdir(self.cached_dir)]

    def store(self, source, articles):
        """
        Writes articles in file by source
        """
        with open(self.source_to_path(source), 'w') as file:
            ls = []
            for article in articles:
                ls.append(self.__article_to_dict(article))
            json.dump(ls, file)

    def load(self, source):
        """
        Loads articles from file by source
        """
        return self.load_by_path(self.source_to_path(source))

    def load_by_path(self, path):
        """
        Loads articles from file by path
        """
        if not os.path.exists(path):
            return []
        with open(path, 'r') as file:
            ls = []
            for item in json.load(file):
                ls.append(self.__article_from_dict(item))
            return ls

    def __article_from_dict(self, item):
        """
        Construct article from inner storage dict
        """
        return Article(item["Title"], item["Link"], datetime.fromisoformat(item["Date"]))

    def __article_to_dict(self, article):
        """
        Construct inner storage dict from article
        """
        return {
            "Title": article.title,
            "Date": article.date.isoformat(),
            "Link": article.link
        }

    def all_items(self):
        """
        Loads articles from all sources
        """
        result = []
        for path in self.list_of_paths():
            result.extend(self.load_by_path(path))
        return result

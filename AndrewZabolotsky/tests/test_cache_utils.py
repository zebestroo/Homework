import os
import json
import shutil
import unittest
import rss_reader
from datetime import datetime
from rss_reader import cache_utils


class TestCacheUtils(unittest.TestCase):
    def setUp(self):
        self.cache = cache_utils.Cache("dir_cache")
        self.date = datetime.today()
        self.source = "https://news.yahoo.com/rss/"
        self.data = rss_reader.rss_reader.Feed(
            "Title", "Link", [rss_reader.rss_reader.Article("Title", "Link", self.date)])
        self.data_dict = {"Title": "Title", "Link": "Link", "Articles": [{
            "Title": "Title",
            "Date": self.date.isoformat(),
            "Link": "Link"
        }], "Image": None}

    def tearDown(self):
        shutil.rmtree("dir_cache")

    def test_source_to_path(self):
        self.assertEqual(os.path.join("dir_cache", "8d84bc9b197af8ffd5c5d97fccf4739b"), self.cache._source_to_path(self.source))

    def test_list_of_paths(self):
        urls = ["https://news.google.com/rss/", "https://news.yahoo.com/rss/"]
        paths = set([self.cache._source_to_path(url) for url in urls])
        for path in paths:
            file = open(path, "w")
            file.close()
        self.assertEqual(paths, set(self.cache._list_of_paths()))

    def test_store(self):
        self.cache.store(self.source, self.data)
        with open(self.cache._source_to_path(self.source), 'r') as file:
            self.assertEqual(self.data_dict, json.load(file))

    def test_load(self):
        with open(self.cache._source_to_path(self.source), 'w') as file:
            json.dump(self.data_dict, file)
        self.assertEqual(self.data, self.cache.load()[0])

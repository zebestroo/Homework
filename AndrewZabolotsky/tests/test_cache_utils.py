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
        self.data = [rss_reader.rss_reader.Article("Title", "Link", self.date)]
        self.data_dict = [{
            "Title": "Title",
            "Date": self.date.isoformat(),
            "Link": "Link"
        }]

    def tearDown(self):
        shutil.rmtree("dir_cache")

    def test_source_to_path(self):
        self.assertEqual(os.path.join("dir_cache", "news.yahoo.com"), self.cache.source_to_path(self.source))

    def test_list_of_paths(self):
        urls = ["https://news.google.com/rss/", "https://news.yahoo.com/rss/"]
        paths = [self.cache.source_to_path(url) for url in urls]
        for path in paths:
            file = open(path, "w")
            file.close()
        self.assertEqual(paths, self.cache.list_of_paths())

    def test_store(self):
        self.cache.store(self.source, self.data)
        with open(self.cache.source_to_path(self.source), 'r') as file:
            self.assertEqual(self.data_dict, json.load(file))

    def test_all_items(self):
        with open(self.cache.source_to_path(self.source), 'w') as file:
            json.dump(self.data_dict, file)
        self.assertEqual(vars(self.data[0]), vars(self.cache.all_items()[0]))

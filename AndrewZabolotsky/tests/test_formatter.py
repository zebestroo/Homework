import unittest
import json
import rss_reader
from rss_reader import formatter
import datetime


class TestArticleFormatter(unittest.TestCase):
    def setUp(self):
        """Configure Article item for further tests"""
        self.item = rss_reader.rss_reader.Article("Title", "http://link", datetime.datetime(2021, 10, 14, 21, 17, 20))

    def test_json_format(self):
        """Tests item is correctly serialized to json format"""
        form = formatter.ArticleFormatter(True)
        dc = {
            "Title": "Title",
            "Date": "2021-10-14 21:17:20",
            "Link": "http://link"
        }
        self.assertEqual(json.dumps(dc), form.format(self.item))

    def test_console_format(self):
        """Tests item is correctly serialized to console format"""
        form = formatter.ArticleFormatter(False)
        self.assertEqual("\nTitle: Title\nDate: 2021-10-14 21:17:20\nLink: http://link", form.format(self.item))

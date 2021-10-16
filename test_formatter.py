import unittest
import json
import article
import formatter
import datetime


class TestArticleFormatter(unittest.TestCase):
    def setUp(self):
        self.item = article.Article("Title", "http://link", datetime.datetime(2021, 10, 14, 21, 17, 20))

    def test_json_format(self):
        form = formatter.ArticleFormatter(True)
        dc = {
                "Title": "Title",
                "Date": "2021-10-14 21:17:20",
                "Link": "http://link"
            }
        self.assertEqual(json.dumps(dc), form.format(self.item))

    def test_console_format(self):
        form = formatter.ArticleFormatter(False)
        self.assertEqual("\nTitle: Title\nDate: 2021-10-14 21:17:20\nLink: http://link", form.format(self.item))


if __name__ == '__main__':
    unittest.main()

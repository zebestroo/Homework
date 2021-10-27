import unittest
import json
import rss_reader
from rss_reader.rss_reader import Feed, Article
from rss_reader.formatter import HtmlPrinter, Fb2Printer
import datetime


class TestHtmlPrinter(unittest.TestCase):
    def setUp(self):
        self.date = datetime.datetime.today()
        self.feed = Feed("Title", "Link", [Article("Title", "Link", self.date)], "image.png")

    def test_print(self):
        expected = f"""
<!DOCTYPE html>
<html>
<body>
<h1>Title</h1>
<img src="image.png"></img>
<div>
<h3>Title</h3>
<p>{self.date}</p>
<a href="Link">Link</a>
</div>
</body>
</html>""".replace("\n", "")
        self.assertEqual(expected, HtmlPrinter("")._print([self.feed]))


class TestFb2Printer(unittest.TestCase):
    def setUp(self):
        self.date = datetime.datetime.today()
        self.feed = Feed("Title", "Link", [Article("Title", "Link", self.date)], "image.png")

    def test_print(self):
        expected = f"""
<?xml version="1.0" encoding="utf-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">
<body>
<section>
<p><strong>Title</strong></p>
<empty-line/>
<p>Title</p>
<p>{self.date}</p>
<p><a l:href="Link">Link</a></p>
</section>
</body>
</FictionBook>""".replace("\n", "")
        self.assertEqual(expected, Fb2Printer("")._print([self.feed]))

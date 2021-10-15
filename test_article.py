import article
import datetime
import unittest
import xml.etree.ElementTree as ET


class TestArticle(unittest.TestCase):
    def test_init(self):
        item = """
                <item>
                    <title>Title</title>
                    <link>https://news.yahoo.com</link>
                    <pubDate>2021-10-14T21:17:20Z</pubDate>
                </item>
                """
        pub = article.Article(ET.fromstring(item))
        self.assertEqual(pub.title, 'Title')
        self.assertEqual(pub.link, 'https://news.yahoo.com')
        self.assertEqual(pub.date, datetime.datetime(2021, 10, 14, 21, 17, 20))


if __name__ == '__main__':
    unittest.main()

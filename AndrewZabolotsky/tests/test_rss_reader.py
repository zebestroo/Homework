import unittest
import requests_mock
from rss_reader import rss_reader


class TestRssReader(unittest.TestCase):
    def setUp(self):
        self.feed = rss_reader.Feed(title="Title",
                                    image="http://l.yimg.com/image.png",
                                    link="https://www.yahoo.com/news",
                                    articles=[rss_reader.Article(
                                        "Title", "https://news.yahoo.com/", "2021-10-29T13:43:21Z")]
                                    )

        self.xml = """<channel>
                        <title>Title</title>
                        <link>https://www.yahoo.com/news</link>
                        <pubDate>Sat, 30 Oct 2021 06:11:11 -0400</pubDate>
                        <image>
                            <url>http://l.yimg.com/image.png</url>
                        </image>
                        <item>
                            <title>Title</title>
                            <link>https://news.yahoo.com/</link>
                            <pubDate>2021-10-29T13:43:21Z</pubDate>
                        </item>
                    </channel>"""

    def test_parse_feed(self):
        self.assertEqual(self.feed, rss_reader.parse_feed(self.xml))

    def test_parse_feed_exception(self):
        with self.assertRaises(Exception) as context:
            rss_reader.parse_feed("")
        self.assertTrue("Unable to parse feed" in str(context.exception))

    def test_fetch_feed_exception(self):
        with self.assertRaises(Exception) as context:
            rss_reader.fetch_feed("")
        self.assertTrue("Unable to connect" in str(context.exception))

    @requests_mock.mock()
    def test_fetch_feed(self, mock):
        mock.get("http://feeds/rss/", text=self.xml)
        self.assertEqual(rss_reader.fetch_feed("http://feeds/rss/"), self.feed)

    @requests_mock.mock()
    def test_fetch_feed_with_failed_request(self, mock):
        mock.get("http://feeds/rss/", status_code=400, text=self.xml)
        with self.assertRaises(Exception) as context:
            rss_reader.fetch_feed("http://feeds/rss/")
        self.assertTrue("Unable to connect" in str(context.exception))

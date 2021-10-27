"""Helper functions"""
import requests
import datetime
import logging
from bs4 import BeautifulSoup


class Article:
    """Data container for parsed article."""

    def __init__(self, title, link, date):
        """
        :param str title: Title of the article
        :param str link: Link of the article
        :param datetime data: Published date of the article
        """
        self.title = title
        self.link = link
        self.date = date

    def __eq__(self, other):
        return (self.title == other.title and
                self.link == other.link and
                self.date == other.date)


class Feed:
    """Data container for parsed feed."""

    def __init__(self, title=None, link=None, articles=None, image=None):
        """
        :param str title: Title of the feed 
        :param str link: Link of the feed
        :param list articles: List of articles
        :param str image: URL of image 
        """
        self.title = title
        self.link = link
        self.articles = articles
        self.image = image

    def __eq__(self, other):
        return (self.title == other.title and
                self.link == other.link and
                self.image == other.image and
                self.articles == self.articles)


def parse_feed(xml):
    """
    Parses feed from xml
    """
    def parse_date(date):
        """
        Parses date from string in configured formats
        """
        for fmt in ['%Y-%m-%dT%H:%M:%SZ', '%a, %d %b %Y %H:%M:%S %Z']:
            try:
                return datetime.datetime.strptime(date, fmt)
            except Exception:
                pass
        raise Exception(f"Unknown date format {date}")

    try:
        soup = BeautifulSoup(xml, 'xml')
        feed = Feed(articles=[])
        for item in soup.find_all("item"):
            feed.articles.append(Article(item.title.text, item.link.text, parse_date(item.pubDate.text)))
        channel = soup.find('channel')
        if channel.title:
            feed.title = channel.title.text
        if channel.link:
            feed.link = channel.link.text
        if channel.image and channel.image.url:
            feed.image = channel.image.url.text
        return feed
    except Exception as e:
        logging.error(e)
        raise Exception("Unable to parse feed")


def fetch_feed(source):
    """
    Fetches news from source

    :param str source: URL to fetch from
    """
    try:
        logging.info(f"Fetching feed from {source}")
        response = requests.get(source)
        response.raise_for_status()
        return parse_feed(response.text)
    except requests.exceptions.RequestException as e:
        logging.error(e)
        raise Exception(f"Unable to connect {source}")

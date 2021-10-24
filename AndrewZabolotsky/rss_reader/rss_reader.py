"""Helper functions"""
import requests
import datetime
from bs4 import BeautifulSoup
from html import unescape


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


def print_news(articles, date, limit, formatter):
    """
    Print news to stdout according limit by means of formatter.

    :param list articles: List of articles to output
    :param datetime.date date: Date of publishing
    :param int limit: Limit number of articles to process, if None -> all avaliable
    :param ArticleFormatter formatter: Output formatter
    """
    if date:
        articles = list(filter(lambda pub: pub.date.date() == date, articles))
        if not articles:
            raise Exception(f"No news for specified date: {date}")
    for pub in articles[:limit]:
        print(formatter.format(pub))


def fetch_articles(source):
    """
    Fetches news from source

    :param str source: URL to fetch from
    """

    def parse_date(date):
        for fmt in ['%Y-%m-%dT%H:%M:%SZ', '%a, %d %b %Y %H:%M:%S %Z']:
            try:
                return datetime.datetime.strptime(date, fmt)
            except Exception:
                pass
        raise Exception(f"Unknown date format {date}")

    response = requests.get(source)
    soup = BeautifulSoup(response.text, 'xml')
    articles = []
    for item in soup.find_all("item"):
        articles.append(Article(item.title.text, item.link.text, parse_date(item.pubDate.text)))
    return articles

"""Provides Article class."""
import datetime


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

    @staticmethod
    def parse_from_xml(item):
        """
        Returns Article object parsed from item.
        
        :param xml item: Contains title, date and link inner fields 
        """
        title = None
        date = None
        link = None
        for child in item:
            if child.tag == 'title':
                title = child.text
            elif child.tag == 'link':
                link = child.text
            elif child.tag == 'pubDate':
                date = datetime.datetime.strptime(child.text, '%Y-%m-%dT%H:%M:%SZ')
        return Article(title, link, date)

"""Provides Arcticle formatter."""
import json


class ArticleFormatter:
    """Formats Article according to params."""

    def __init__(self, js):
        """
        :param boolean js: Specifies output format(if passed -> json, otherwise -> plain)
        """
        self.js = js

    def format(self, article):
        """
        Converts article into str according specified format

        :param Article article: Object to convert
        """
        if self.js:
            return json.dumps({
                "Title": article.title,
                "Date": article.date.isoformat(sep=' '),
                "Link": article.link
            })
        else:
            return f'\nTitle: {article.title}\nDate: {article.date}\nLink: {article.link}'

"""Provides Arcticle formatter."""
import logging
import json
from yattag import Doc
from termcolor import colored


def print_to_console_as_json(feeds):
    """
    Converts article into str according specified format

    :param Article article: Object to convert
    """
    dc = []
    for feed in feeds:
        obj = {"Title": feed.title,
               "Link": feed.link,
               "Image": feed.image,
               "Articles": [{
                   "Title": article.title,
                   "Date": article.date.isoformat(sep=' '),
                   "Link": article.link
               } for article in feed.articles]}
        dc.append(obj)
    print(json.dumps(dc))


def print_to_console(feeds):
    for feed in feeds:
        print(f'\n\t\tTitle: {feed.title}')
        print(f'\t\tLink: {feed.link}')
        for article in feed.articles:
            print(f'\nTitle: {article.title}')
            print(f'Date: {article.date}')
            print(f'Link: {article.link}')


def print_to_console_colorized(feeds):
    for feed in feeds:
        print(colored(f'\n\t\tTitle: {feed.title}', 'red'))
        print(colored(f'\t\tLink: {feed.link}', 'green'))
        for article in feed.articles:
            print(colored(f'\nTitle: ', 'red') + article.title)
            print(colored(f'Date: ', 'green') + str(article.date))
            print(colored(f'Link: ', 'cyan') + article.link)


class Printer:
    def __init__(self, path):
        self.path = path

    def _print(self, articles):
        return ""

    def dump(self, feeds):
        with open(self.path, 'w') as file:
            logging.debug(f"Dumping feeds to {self.path}")
            file.write(self._print(feeds))


class HtmlPrinter(Printer):
    """
    Dump feeds in html format in file
    """

    def __init__(self, path):
        super().__init__(path)

    def _print(self, feeds):
        doc, tag, text, line = Doc().ttl()
        doc.asis('<!DOCTYPE html>')
        with tag('html'), tag('body'):
            for feed in feeds:
                if feed.title:
                    line('h1', feed.title)
                if feed.image:
                    line('img', "", src=feed.image)
                for pub in feed.articles:
                    with tag('div'):
                        line('h3', pub.title)
                        line('p', str(pub.date))
                        line('a', pub.link, href=pub.link)
        return doc.getvalue()


class Fb2Printer(Printer):
    """
    Dump feeds in fb2 format in file
    """

    def __init__(self, path):
        super().__init__(path)

    def _print(self, feeds):
        doc, tag, text, line = Doc().ttl()
        ext = 'xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink"'
        doc.asis('<?xml version="1.0" encoding="utf-8"?>')
        with tag('FictionBook', ext), tag('body'):
            for feed in feeds:
                with tag('section'):
                    if feed.title:
                        with tag('p'):
                            line('strong', feed.title)
                    for pub in feed.articles:
                        doc.asis("<empty-line/>")
                        line('p', pub.title)
                        line('p', str(pub.date))
                        with tag('p'):
                            line('a', pub.link, f'l:href="{pub.link}"')
        return doc.getvalue()

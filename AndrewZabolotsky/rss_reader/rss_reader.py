#!/usr/bin/env python
"""One-shot command-line RSS reader."""
import xml
import xml.etree.ElementTree as ET
import requests
from .article import Article


def print_news(source, logger, limit, formatter):
    """
    Fetches news from source and print them out to stdout according limit by means of formatter.

    :param str source: URL to read from
    :param RootLogger logger: Object to print logs
    :param int limit: Limit number of articles to process, if None -> all avaliable
    :param ArticleFormatter formatter: Output formatter
    """
    try:
        response = requests.get(source)
        root = ET.fromstring(requests.utils.get_unicode_from_response(response))
        articles = [Article.parse_from_xml(item) for item in root[0] if item.tag == 'item'][:limit]
        for pub in articles:
            print(formatter.format(pub))
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        logger.fatal(f"not able to connect to {source}")
    except xml.etree.ElementTree.ParseError:
        logger.fatal(f"not able to parse {source}, is it RSS?")

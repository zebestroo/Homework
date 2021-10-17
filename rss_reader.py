#!/usr/bin/env python
"""One-shot command-line RSS reader."""
import xml
import xml.etree.ElementTree as ET
from formatter import ArticleFormatter
import requests
import argparse
import logging
import article


def parse_args():
    """Returns parsed command-line arguments."""
    def check_positive(value):
        """
        Verifies that passed value is positive.

        :param str value: Argument to verify
        """
        try:
            ivalue = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
        return ivalue
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
    parser.add_argument('source', type=str, help='RSS URL')
    parser.add_argument('--version', action='version', version='Version 1')
    parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
    parser.add_argument('--verbose', action='store_true', help='Outputs verbose status messages')
    parser.add_argument('--limit', type=check_positive, help='Limit news topics if this parameter provided')
    return parser.parse_args()


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
        articles = [article.Article.parse_from_xml(item) for item in root[0] if item.tag == 'item'][:limit]
        for pub in articles:
            print(formatter.format(pub))
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        logger.fatal(f"not able to connect to {source}")
    except xml.etree.ElementTree.ParseError:
        logger.fatal(f"not able to parse {source}, is it RSS?")


if __name__ == '__main__':
    args = parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.WARNING)
    logger = logging.getLogger()
    logger.debug(' '.join([f'{k}={v}' for k, v in vars(args).items()]))
    print_news(args.source, logger, args.limit, ArticleFormatter(args.json))

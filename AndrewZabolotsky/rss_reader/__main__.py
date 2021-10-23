import argparse
import logging
from .rss_reader import print_news
from .formatter import ArticleFormatter


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
    parser = argparse.ArgumentParser(prog='rss_reader', description='Pure Python command-line RSS reader.')
    parser.add_argument('source', type=str, help='RSS URL')
    parser.add_argument('--version', action='version', version='Version 1')
    parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
    parser.add_argument('--verbose', action='store_true', help='Outputs verbose status messages')
    parser.add_argument('--limit', type=check_positive, help='Limit news topics if this parameter provided')
    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.WARNING)
    logger = logging.getLogger()
    logger.debug(' '.join([f'{k}={v}' for k, v in vars(args).items()]))
    print_news(args.source, logger, args.limit, ArticleFormatter(args.json))


if __name__ == "__main__":
    main()

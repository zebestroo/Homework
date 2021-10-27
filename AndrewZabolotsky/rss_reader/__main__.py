"""One-shot command-line RSS reader."""
import argparse
import coloredlogs
import logging
import datetime
from importlib.metadata import version
from .cache_utils import Cache
from .rss_reader import fetch_feed
from .formatter import HtmlPrinter, Fb2Printer, print_to_console, print_to_console_as_json, print_to_console_colorized


def parse_args():
    """
    Returns parsed command-line arguments
    """
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

    def check_date(date):
        """
        Verifies passed date format
        """
        return datetime.datetime.strptime(date, "%Y%m%d").date()

    parser = argparse.ArgumentParser(prog='rss_reader', description='Pure Python command-line RSS reader.')
    parser.add_argument('--source', type=str, help='RSS URL')
    parser.add_argument('--to-html', type=str, metavar="PATH", help='Outputs news to file in HTML format')
    parser.add_argument('--to-fb2', type=str, metavar="PATH", help='Outputs news to file in FB2 format')
    parser.add_argument('--version', action='version', version="Version " + version("rss_reader_by_Andrew_Zabolotsky"))
    parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
    parser.add_argument('--colorize', action='store_true', help='Colorize output')
    parser.add_argument('--verbose', action='store_true', help='Outputs verbose status messages')
    parser.add_argument('--limit', type=check_positive, help='Limit news topics if this parameter provided')
    parser.add_argument('--date', type=check_date, help='Defines date news for catching')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.colorize:
        coloredlogs.install(level="DEBUG" if args.verbose else "INFO")
    else:
        logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    logging.debug(' '.join([f'{k}={v}' for k, v in vars(args).items()]))

    try:
        cache = Cache()
        if args.source and not args.date:
            feed = fetch_feed(args.source)
            cache.store(args.source, feed)
        feeds = cache.load(source=args.source, date=args.date, limit=args.limit)
        if not feeds and args.date:
            print(f"No news for {args.date} date")
            return

        if args.to_html:
            HtmlPrinter(args.to_html).dump(feeds)
        if args.to_fb2:
            Fb2Printer(args.to_fb2).dump(feeds)
        if args.json:
            print_to_console_as_json(feeds)
        elif args.colorize:
            print_to_console_colorized(feeds)
        else:
            print_to_console(feeds)
    except Exception as exception:
        logging.fatal(exception)


if __name__ == "__main__":
    main()

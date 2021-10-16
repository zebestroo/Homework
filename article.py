import datetime


class Article:
    def __init__(self, title, link, date):
        self.title = title
        self.link = link
        self.date = date

    @staticmethod
    def parse_from_xml(item):
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

    def __str__(self):
        return f'\nTitle: {self.title}]\nDate: {self.date}\nLink: {self.link}'

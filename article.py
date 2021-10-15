import datetime


class Article:
    def __init__(self, item):
        for child in item:
            if child.tag == 'title':
                self.title = child.text
            elif child.tag == 'link':
                self.link = child.text
            elif child.tag == 'pubDate':
                self.date = datetime.datetime.strptime(child.text, '%Y-%m-%dT%H:%M:%SZ')

    def __str__(self):
        return f'\nTitle: {self.title}]\nDate: {self.date}\nLink: {self.link}'

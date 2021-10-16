import json


class ArticleFormatter:
    def __init__(self, js):
        self.js = js

    def format(self, article):
        if self.js:
            return json.dumps({
                "Title": article.title,
                "Date": str(article.date),
                "Link": article.link
                })
        else:
            return f'\nTitle: {article.title}\nDate: {article.date}\nLink: {article.link}'

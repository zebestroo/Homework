class HistoryDict:

    def __init__(self, dc):
        self.dc = dc
        self.ls = []

    def set_value(self, key, value):
        self.dc[key] = value
        if len(self.ls) < 10:
            self.ls.append(key)
        else:
            self.ls.pop(0)
            self.ls.append(key)

    def get_history(self):
        print(self.ls)

d = HistoryDict({"foo" : 42})
d.set_value("bar", 43)
d.get_history()

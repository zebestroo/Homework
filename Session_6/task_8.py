class Pagination:

    def __init__(self, st, num):
        self.num = num
        self.str = st
        self.lst = []
        i = 0
        j = 0
        while i < len(st)//num:
            self.lst.append(st[j:j+num])
            j += num
            i += 1
        self.lst.append(st[j:]) 
        self.page_count = len(self.lst)
        self.item_count = len(st)

    def count_items_on_page(self, index):
        if index < len(self.lst):
            print(len(self.lst[index]))
            return len(self.lst[index])
        else:
            print("Invalid index. Page is missing")

    def find_page(self, st):
        if st in self.str:
            ls = []
            i = 1
            pos = self.str.find(st)
            while i*self.num < pos+1:
                i += 1
            ls.append(i-1)
            i = 1
            pos2 = self.str.rfind(st)
            pos2 += len(st)-1
            while i*self.num < pos2:
                i += 1
            ls.append(i-1)
            print(ls)
        else:
            print(f'"{st}" is missing on the page')
    def display_page(self, index):
        if index < len(self.lst):
            print(self.lst[index])
            return self.lst[index]

pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)
pages.count_items_on_page(0)
pages.count_items_on_page(3)
pages.count_items_on_page(4)
pages.find_page('Your')
pages.find_page('e')
pages.find_page('beautiful')
pages.find_page('great')
pages.display_page(0)




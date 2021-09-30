def get_digits(num):
    st = str(num)
    i = 0
    tp = []
    while i < len(st):
       tp.append(st[i])
       i += 1
    tp = tuple(tp)
    return tp
print(get_digits(87178291199))

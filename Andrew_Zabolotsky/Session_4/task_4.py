def split_by_index(s, indexes):
    i = 0
    ls = []
    for j in indexes:
        if isinstance(j, int):
            ls.append(s[i:j])
            i = j
        else:
            continue
    if s[i:] != '':
        ls.append(s[i:])
    return ls


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))

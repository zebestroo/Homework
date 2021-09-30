def get_pairs(ls):
    List = []
    if len(ls) > 1:
        i = 0
        while i < len(ls)-1:
            List.append(tuple([ls[i], ls[i+1]]))
            i += 1
        return List
    else:
        return None

print(get_pairs([1, 2, 3, 8, 9]))

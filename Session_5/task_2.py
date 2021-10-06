import re
def most_common_words(filepath, number_of_words=3):
    fl = open(filepath)
    dc = {}
    ls = fl.readlines()
    ls_wds = []
    for i in ls:
        for j in re.split(", |[. \n]", i):
            if j.lower() in dc:
                dc[j.lower()] += 1
            else:
                dc[j.lower()] = 0
    dc.pop('')
    j = 0
    while j < number_of_words:
        max_el = max(dc.values())
        for i in dc:
            if dc[i] == max_el:
                ls_wds.append(i)
                dc.pop(i)
                break
        j += 1
    return ls_wds

print(most_common_words('../data/lorem_ipsum.txt'))

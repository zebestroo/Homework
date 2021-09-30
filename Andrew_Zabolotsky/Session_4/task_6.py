def get_longest_word(s):
    i = ''
    for j in s.split():
        if len(j) > len(i):
            i = j
    return i
print(get_longest_word('Any pythonista like namespaces a lot.'))

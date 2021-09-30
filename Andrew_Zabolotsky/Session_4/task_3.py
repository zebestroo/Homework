st = "My new string"
def func(st, sep):
    i = 0
    ls = []
    while i < len(st):
        if st.find(sep) != -1:
            ls.append(st[i:st.find(sep)])
            st = st[len(st[i:st.find(sep)]) + len(sep):]
        else:
            ls.append(st)
            return ls
        i = 0
print(func(st, ' new '))

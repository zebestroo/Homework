s = 'Oh, it is python'
st = dict()
s = s.lower()
for i in s:
    if i in st:
        st[i] += 1
    else:
        st[i] = 1
print(st)

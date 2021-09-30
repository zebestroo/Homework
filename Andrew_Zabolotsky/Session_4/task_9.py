import string
def test_1_1(*strings):
    st = set(strings[0])
    for i in strings:
        st =st.intersection(set(i))
        
    return sorted(st)

print(test_1_1("hello", "world", "python"))

def test_1_2(*strings):
    st = set()
    for i in strings:
        st = st.union(set(i))
        
    return sorted(st)

print(test_1_2("hello", "world", "python"))

def test_1_3(*strings):
    dc = {}
    nst = set()
    for i in string.ascii_lowercase:
        dc[i] = 0
    for st in strings:
        for i in st:
            dc[i] += 1
    for i in dc.keys():
        if dc[i] >= 2:
            nst.add(i)

    return sorted(nst)


print(test_1_3("hello", "world", "python"))

def test_1_4(*strings):
    st = set()
    for i in strings:
        st = st.union(set(i))
    st = set(string.ascii_lowercase).difference(st) 
    return sorted(st)

print(test_1_4("hello", "world", "python"))

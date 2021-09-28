a = 2
b = 4
c = 3
d = 7
def func(num):
    i = 0
    while num/(pow(10, i)) >= 1:
        i += 1
    return str(num) + ' '*(8-i)
st = ""
st += 8*' '
for i in range(c, d+1):
    st += func(i)
st += '\n'

for i in range(a, b+1):
    st += func(i)
    for j in range(c, d+1):
        st += func(i*j)
    st += '\n'
print(st)


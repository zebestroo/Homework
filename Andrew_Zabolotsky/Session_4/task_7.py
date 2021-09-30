def foo(ls):
    count = 1
    for i in ls:
        count *= i
    nls = []
    for i in ls:
        nls.append(int(count/i))
    return nls
print(foo([1, 2, 3, 4, 5]))


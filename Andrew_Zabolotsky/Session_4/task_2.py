def is_polydr(st):
    i = 0
    while i < len(st)/2:
        if st[i] != st[-i-1]:
            return False
        i += 1
    return True

print(is_polydr("12345321"))

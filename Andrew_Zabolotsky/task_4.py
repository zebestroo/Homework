num = input()
num = int(num)
st = set()
i = 1
while i*i < num:
    if num % i == 0:
        st.add(i)
        st.add(int(num/i))
        i += 1
    else:
        i += 1
print(sorted(st))

    

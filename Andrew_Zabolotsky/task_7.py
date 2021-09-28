tp = (1, 2, 3, 4)
count = 0
s = 1 
for i in tp:
   count += i * (pow(10, len(tp)-s))
   s += 1
print(count)

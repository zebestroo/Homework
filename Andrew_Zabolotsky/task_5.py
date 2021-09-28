dc = {1:"cat", 3:"cow", 4:"horse", 2:"dog"}
new_dict = {}
for i in sorted(dc):
    new_dict[i] = dc[i]
print(new_dict)

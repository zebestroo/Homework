ls = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
st = set()
for i in ls:
    for j in i:
        st.add(i[j])
print(st)
        

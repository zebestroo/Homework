def generate_squares(num):
    dc ={}
    for i in range(num):
        dc[i+1] = pow(i+1, 2)
    return dc

print(generate_squares(5))

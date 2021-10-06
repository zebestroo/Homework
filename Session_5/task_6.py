res = 0
def call_once(func):
    def new_f(a, b):
        global res
        if res == 0:
            res = func(a, b)
            return res
        else:
            return res
    return new_f

@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))

res = None

def remember_result(sum_func):
    def last_res(*args):
        global res
        print(f"Last result = '{res}'")
        res = sum_func(*args)
    return last_res

@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
sum_list("abc", "cde")
#sum_list(3, 4, 5) / original function "sum_list" is not suitable for use with integers
#I used original function from the task

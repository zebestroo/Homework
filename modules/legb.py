a = "I am global variable!"


def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():

        nonlocal a# = "I am local variable!"
        # For print global a, we need to change "nonlocal" to "global" and result will be "I am global variable"
        print(a)
    inner_function()

enclosing_function()

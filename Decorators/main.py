
def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print("display function ran")

decorated_display = decorator_function(display)
decorated_display()
print("----------")
#Or The other way

def decorator_function2(original_function):
    def wrapper_function():
        print("i too ran before the og_function")
        return original_function()
    return wrapper_function

@decorator_function2
def display2():
    print("display2 has ran, ggs")

display2()
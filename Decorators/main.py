

def decorator_function(original_function:function):
    def wrapper_function():
        return original_function()
    return wrapper_function




mikko_myfunc = decorator_function("Mikko")
hi_myfunc = decorator_function("Hello Hi")

mikko_myfunc()
hi_myfunc()
from datetime import datetime

def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print("display function ran")

#@Function name is the same as this 
decorated_display = decorator_function(display)

decorated_display()
print("----------\n")
#Or The other way

def decorator_function2(original_function):
    def wrapper_function():
        print("I ran before the og_function")
        return original_function()
    return wrapper_function

@decorator_function2
def salute_you():
    print("Amazing gainz you got there")



#Passing arguments the real way
#-------------
print("---------\n")

def decorator_function_with_arguments(original_function):
    #args and kwargs permit any data to flow trough
    def wrapper_function(*args, **kwargs):
        print("\nwrapper executed this before {}".format(original_function.__name__))
        print(f"I too know the arguments: {args}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function_with_arguments
def display_info(name: str,age:int):
    print(f"display info ran with arguments {name} and {age}")


@decorator_function_with_arguments
def give_year(name:str):
    print(f"Hello {name}, the time is:",datetime.now())



give_year("Mikko")

display_info("John",22)





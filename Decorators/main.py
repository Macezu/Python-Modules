from datetime import datetime

print("------")
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
print("----------")
#Or The other way

def decorator_function2(original_function):
    def wrapper_function():
        print("I ran before the og_function")
        return original_function()
    return wrapper_function

@decorator_function2
def salute_you():
    print("Amazing gainz you got there")

salute_you()

#Passing arguments the real way
#-------------
print("---------")

def decorator_function_with_arguments(original_function):
    #args and kwargs permit any data to flow trough
    def wrapper_function(*args, **kwargs):
        print("\nwrapper executed this before {}".format(original_function.__name__))
        print(f"I too know the arguments if given: {args}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function_with_arguments
def display_info(name: str,age:int):
    print(f"display info ran with arguments {name} and {age}")


@decorator_function_with_arguments
def give_year(name:str):
    print(f"Hello {name}, the time is:",datetime.now())

@decorator_function_with_arguments
def hello_world():
    print("Hello world, i dont use aguments")

give_year("Mikko")

display_info("John",22)

hello_world()

#Class decorator
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    #The call method works like the wrapper function from before
    def __call__(self, *args, **kwargs):
        print("\nCall method excecuted this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display_info_class(name : str):
    print(f"Hello {name}, im using decorator class")

display_info_class("Ismo")
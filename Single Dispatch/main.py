from functools import singledispatch


@singledispatch
def my_func(*args):
    print(f"Default myfunc {args}")


@my_func.register
def my_func_int(*args: int):
    print(f"arg is an int {args}")


@my_func.register
def my_func_list_version(*args: list):
    for item in args:
        print(f"The items are {item}")

def main():
    my_func("hi")
    my_func(23)
    my_func(["A","B","C"])



if __name__ == "__main__":
    main()
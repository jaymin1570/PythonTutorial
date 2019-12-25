from functools import wraps
def print_function_data(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        print(f"you are calling {any_function.__name__} function")
        print(f"{any_function.__doc__}")
        return any_function(*args,**kwargs)
    return wrapper_function


@print_function_data
def addition(a,b):
    '''this function takes two numbers as arguments and return their sum'''
    return a+b

print(addition(4,5))


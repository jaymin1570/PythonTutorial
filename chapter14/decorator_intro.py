# Decorator - enhance the functionality of other function
# @ use for decorator # @ means:-synthetic suger

def decorator_function(any_function):
    def wrapper_function():
        print("this is awesome function !")
        any_function()
    return wrapper_function
@decorator_function # shortcut
def func1():
    print('this is function 1')
func1()
# var = decorator_function(func1)
# var()

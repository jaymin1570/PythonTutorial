# only_int_allows
from functools import wraps
def only_int_allows(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return any_function(*args,**kwargs)
        print("invalid arguments")
        # print(any_function.__name__)
        # data_type=[]
        # for arg in args:
        #     data_type.append(type(arg)==int)
        # if all(data_type):
        #     return any_function(*args,**kwargs)
        # else:
        #     print("Invalid argument")
    return wrapper_function
@only_int_allows
def add_all(*args):
    total =0
    for i in args:
        total+=i
    return total
print(add_all(1,2,3,4,5))

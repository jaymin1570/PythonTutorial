from functools import wraps

def only_data_type_allow(data_type):
    def decorator(any_function):
        @wraps(any_function)
        def wrapper_function(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return any_function(*args,**kwargs)
            print("invalid arguments")
        return wrapper_function
    return decorator
@only_data_type_allow(str)
def string_join(*args):
    string= ''
    for i in args:
        string +=i
    return string
print(string_join('jaymin', 'makwana','A',2))
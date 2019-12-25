# kwargs (keyword argument)
# ** kwargs (double star operator)

# kwargs as parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
                 print(f"{k} : {v}")

# dictionary unpacking

d={'name':'jaymin','age':2}
func(**d)
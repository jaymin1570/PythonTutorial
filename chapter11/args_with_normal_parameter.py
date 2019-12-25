# *args with noraml parameter

def multiply_num(num,*args):
    print(num,args)
    multiply=1
    for i in args:
        multiply*=i
    return multiply
print(multiply_num(2,7,6))
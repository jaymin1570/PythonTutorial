def multiply_num(*args):
    print(args) # tuples (2,3,4,5)
    multiply=1
    for i in args:
        multiply*=i
    return multiply
num = [2,3,4,5]
print(multiply_num(*num)) # unpack


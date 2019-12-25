# function return two values

def func(int1,int2):
    add = int1 +int2
    mul = int1 * int2
    return add,mul

add, mul = func(5,6)
print(add)
print(mul)

print(func(5,6))
print(type(func(5,6)))

# add, mul = (5,6)
# print(add)
# print(mul)
# lambda expression (anonymous function)

def add(a,b):
    return a+b

print(add)

add2=lambda a,b :a+b
print(add2(2,3))

# built in function map,reduce,filter

multiply= lambda a,b:a*b
print(type(multiply))

print(multiply(3,4))
print(add2)
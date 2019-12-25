# map function 

# numbers = [1,2,3,4] # list comprehension
# s2 = [a**2 for a in numbers]
# print(s2)
# def square(a):
#     return a**2

# square= list(map(lambda a:a**2,numbers))
# print(square)
# print(type(map))

names = ['abc','abcd','abcde']
n =(map(len,names))
for i in n:
    print(i)


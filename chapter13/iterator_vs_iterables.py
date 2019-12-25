# iterator vs iterable

numbers = [1,2,3,4] # itrerables # tuple,string
square =(map(lambda a:a**2,numbers)) # iterator)
print(next(square))
print(next(square))
print(next(square))

# for i in numbers:
#     print(i)
# print('\n')
# for i in square:
#     print(i)

iter_call = iter(numbers)
print(next(iter_call)) #-------->iterator
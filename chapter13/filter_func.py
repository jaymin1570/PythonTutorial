# filter function 

# def is_even(a):
#     return a%2 ==0

numbers=[3,4,2,1,5,6,8,6,7,5,10]
# evens_list = [] 
evens=tuple(filter(lambda a:a%2==0,numbers))
# print(evens)
for i in evens:
    print(i)

# for i in evens:
#     print(evens[i])
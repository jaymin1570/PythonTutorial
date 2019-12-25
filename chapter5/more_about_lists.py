# generate list with range function
# something more about pop method
# index method
# pass list to a function

numbers = list(range(1,11))
number=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

print(f"popped element: {numbers.pop()}")
print(numbers)

print(f"index number: {number.index(1,0,16)}")

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative#[::-1]
    #print(negative)
# negative_list(number)
print(f"negative list is : {negative_list(number)}")
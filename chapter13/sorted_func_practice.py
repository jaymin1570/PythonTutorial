# sorted function 
# mutable and immutable object in python,
# mutable object can be changed after it is created and
#an immutable object can't chaged.

fruits1 = ['grapes','mango','apple']
# sort
fruits1.sort()
print(fruits1)

fruits2=('grapes','mango','apple') # tuple immutable
print(sorted(fruits2))
print(fruits2)
# fruits2.sort()
# print(fruits2)

fruits3 ={'grapes','mango','apple'}
print(sorted(fruits3))
# fruits3.sort()
# print(fruits3)



guitars = [
    {'model':'yamaha f310','price':8400},
    {'model':'faith napture','price':50000},
    {'model':'faith apollo venus','price':35000},
    {'model':'taylor 814ce','price':450000}
]

print(sorted(guitars,key = lambda item:item['price'],reverse=True))

# any ,all function 

number1 = [2,4,6,8,10]
number2 = [1,2,3,4,5,6]

even1 = all([i%2==0 for i in number1])
even2 = any([i%2==0 for i in number2])
print(even1)
print(even2)
print(any([False, False, False, True, False]))
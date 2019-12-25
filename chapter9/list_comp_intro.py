# list comprehension
# with the help of list comprehension we can create of list in one line

# create a list of square from 1 to 10
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)

# square2 = [i **2 for i in range(1,11)]
# print(square2)

# negative = []
# for i in range(1,11):
#     negative.append(-i)

# print(negative)

negative2 = [-i for i in range(1,11)]
print(negative2)

names = ['jaymin' ,'mehul', 'sahal' ,'mahendra']
# new_list = ['j','m','s','m']
# new_list = []
# for i in name:
#     new_list.append(i[0])

# print(new_list)

new_list= [name[0] for name in names]
print(new_list)

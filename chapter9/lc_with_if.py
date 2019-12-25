# list  comprehension with if statement 

# number = list(range(1,11))
# print(number)
 
# even_num =[]
# for num in number:
#     if num%2==0:
#         even_num.append(num)

# print(even_num) 

even_num = [num for num in range(1,11) if num%2==0]
print(even_num)
odd_num = [num for num in range(1,11) if num%2!=0]
print(odd_num)
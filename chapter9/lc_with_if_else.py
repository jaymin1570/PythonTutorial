# list comprehension with if else

nums = [1,2,3,4,5,6,7,8,9,10]

# new_list = []
# for num in nums:
#     if num%2==0:
#         new_list.append(num*2)
#     else:
#         new_list.append(-num)

# print(new_list)

new_list = [num*2 if num%2==0 else -num for num in nums ]
print(new_list)
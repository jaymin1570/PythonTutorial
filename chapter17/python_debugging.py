import pdb # import pdb module
# module - python file contain usefull classes and function worte
# by developer

# According to wikipedia - Debugging is the process of finding and resolving 
# defect or problems within a computer program that prevent correct operation
# of computer software or a system.


# step for debugging
# 1.)set trace
# 2.) execute code line by line

pdb.set_trace()
name = input("please type your name:")
age = int(input("please type your age : "))
print(f"hello {name} your age is {age}")
age2= age +5
print(f" {name} you will be {age2} in next five years ")

# l 
# c
# q
# n
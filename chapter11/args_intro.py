# make flexible function 

# *operator 
# *args

# def total(a,b):
#     return a+b
# print(total(5,4))

def all_total(*args):
    total =0
    for i in args:
        total+=(i)
    return total


print(all_total(5,4,9,10))

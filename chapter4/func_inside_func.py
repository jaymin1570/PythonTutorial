# function indide function 

def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
   # bigger = greater(a,b)
    return greater(greater(a,b),c)

print(greatest(36,35,20))

# kiss ---> keep it simple stupid


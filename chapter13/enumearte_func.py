# we use enumerate function with loop to track position of our
# item in iterable

# how we can do this without enumrate function
names = ['abc','abcdef','jaymin']
# for i in range(len(names)):
#     print(f"{i}----->{names[i]}")

# with enumearte function 
# for pos,name in enumerate(names):
#     print(f"{pos}---> {name}")

def find_pos(l,target):
    for pos,name in enumerate(names):
        if name==target:
            return pos
    return -1

print(find_pos(names,'jaymin'))


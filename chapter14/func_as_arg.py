 # map
def square(a):
    return a**2
l = [1,2,3,4]
print(list(map(lambda a:a**2,l)))

def my_map(func,l):
    new_list= []
    for item in l:
        new_list.append(func(item))
    return new_list
 
print(my_map(square,l))
    


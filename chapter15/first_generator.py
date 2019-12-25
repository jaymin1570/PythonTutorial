# create your first generator with generator function
#1.)generator function
#2.)geneartor comprehension

# 10,1 to 10

def nums(n):
    for i in range(1,n+1):
        yield(i)
# print(nums(10))
print(nums.__name__)
numbers=(nums(10))
for number in numbers:
    print(number)
    
for num in numbers:
        print(num)
# memory -------> (list)-[..............]
# memory -------> (generator)-(2)
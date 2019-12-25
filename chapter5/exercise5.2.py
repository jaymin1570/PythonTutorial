enumbers = list(range(1,11))

def reverse_list(l):
    reverse = []
    for i in range(len(l)):
       s=l.pop()
       reverse.append(s)
        
    return reverse
print(numbers)
print(f"reverse list is :{reverse_list(numbers)}")

# number = [1,2,3,4]
# popped_item = numbers.pop()
# n = []
# n.append(popped_item)
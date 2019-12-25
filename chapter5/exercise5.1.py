numbers =list(range(1,11))
def square_list(l):
    n = []
    for i in l:
        n.append(i*i)
    return n
print(numbers)
print(f"square of list : {square_list(numbers)}")

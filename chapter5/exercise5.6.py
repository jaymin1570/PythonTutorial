
num = [1,2,3,[1,2],[3,4]]
# count = 0
# for i in num:
#     if type(i) == int:
#         count+=1

# print(count)

def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count += 1
    return count
print(sublist_counter(num))

# zip function

l1=[1,31,15,7]
l2=[2,4,6,8]

new_list = []
l = [(1,2),(3,4),(5,6),(7,8)]

l1,l2=list(zip(*l))
print(f"l1={list(l1)}")
print(f"l2={list(l2)}")

for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)

# new_list2 = [pair[0] if pair[0]>pair[1] else pair[1] for pair in zip(l1,l2) ]
# print(new_list2)
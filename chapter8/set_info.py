# set data type
# unorder collection of unique items
# not store list and dictionary

s={1,2,3,2,4,5}
print(s)
print(type(s))

# remove duplicate
# l= [1,2,5,5,5,5,6,3,1,5,4,4,4]
# s2 = list(set(l))
# print(s2)

s.add(9)
print(s)
s.discard(5)

s.remove(3)
print(s)
s.clear
()
print(s)
s1 = s.copy()
print(s1)
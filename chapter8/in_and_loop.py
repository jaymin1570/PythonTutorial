# in keyword in sets and loop

s= {'a','b','c'}

if 'a' in s:
    print("present")
else:
    print("not present")

for item in s:
    print(set(item))

s1 = {1,2,3,4,}
s2 = {3,4,5,7,6,2}
# union | pipe
union_set= s1 | s2
print(union_set)
inter_set =s1 & s2
print(inter_set)
# i _=0
# while i<len(s):
#     print(i)
#     i+=1
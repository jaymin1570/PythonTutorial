name = "jaymin"
for i in range(len(name)):
    print(name[i],i)

name2 = "makwana"
for i in name2:
    print(i)
# string is iterable
# int is not iterable
#num = 10
#for i in range(10):
 #   print(i)

num = input("enter a number : ")
total = 0
for i in num:
    total += int(i)
print(total)
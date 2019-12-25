 
name = input("enter your name : ")
temp_var= ""
for i in range(len(name)):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f" # {name[i] } = {name.count(name[i])}")


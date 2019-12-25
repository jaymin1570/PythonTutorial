name , age = input("enter your name and age(separated by comma) ").split(",")
age = int(age)
if (name[0]=='A'or name[0]=='a') and age >= 10:
    print("you can watch coco movie")
else:
    print("you can't watch coco movie")
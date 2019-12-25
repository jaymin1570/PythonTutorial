def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

num1,num2,num3 = input("enter three number (separated by comma)").split(",")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

print(f"greatest number is : {greatest(num1,num2,num3)}")
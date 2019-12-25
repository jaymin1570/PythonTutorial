def max_num(a,b):
    if a > b:
        return a
    return b

num1,num2 = (input("enter two number (separated by comma):")).split(",")
num1 = int(num1)
num2 = int(num2)
print(f"maximum number is : {max_num(num1,num2)}")
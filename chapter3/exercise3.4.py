# example= "1256" # length =4 last index=3
example = input("enter the number:")
len = len(example)
total = 0
i = 0
while i < len:
    total = total +int(example[i])
    i+=1
print(total)
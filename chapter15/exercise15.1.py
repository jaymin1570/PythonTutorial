
def even_num(n):
    for i in range(2,n+1,2):
        # if i%2==0:
        yield(i)
numbers=even_num(20)
for j in numbers:
    print(j)
for k in numbers:
    print(k)
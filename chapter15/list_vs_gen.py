import time

t1=time.time()
l =[i**2 for i in range(1000000)]
t2=time.time()
print(t2-t1)


t3=time.time()
g=(i**2 for i in range(10000000))
t4=time.time()
print(t4-t3)
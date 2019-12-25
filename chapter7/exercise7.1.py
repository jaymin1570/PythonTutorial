#n = range(1,11)
def cub_finder(n):
    cub ={}
    for i in range(1,n+1):
        cub[i]=i*i*i
        
    return cub

k= int(input("enter a number :"))
print(cub_finder(k))

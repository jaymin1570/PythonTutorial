# list inside list

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 3 item ---> 3 list
print(matrix)
print(matrix[1][0])

for sublist in matrix:
    for i in sublist:
        #n = list(range(i))
        print(i)



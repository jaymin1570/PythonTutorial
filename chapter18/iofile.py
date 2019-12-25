# read file
# open file
# read method
# seek method
# tell method
# readline method
# readlines method
# close method
 

f = open(r"D:\New folder\file1.txt")
# windows - \
# linux,mac - /


# name, closed (data descriptor)
# print(f.name)
for line in f.readlines()[:2]:
    print(line,end='')

f.close()
print(f.closed)
# lines=f.readlines()
# # print(len(lines))
# for line in lines:
#     print(line,end=)
# print(f'cursor position - {f.tell()}')
# print(f.read())
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(3))
# print(f'cursor position - {f.tell()}')
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f'cursor position - {f.tell()}')
# print(f.read())

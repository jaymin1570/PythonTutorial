l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]

# average=[lambda l1,l2,l3=(i[0]+i[1]+i[2])/3 for i in zip(l1,l2,l3)]
# print(average)

# def average_finder(*args):
#     # print(tuple(*args))
#     print(args)
#     average = []
#     for pair in zip(*args):
#         # print(list(zip(args)))
#         print(tuple(zip(*args)))
#         print(pair)
#         average.append(sum(pair)/len(pair))
#     return average

average_finder= lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]

print(average_finder(l1,l2,l3))
# average2 =[sum(pair)/len(pair) for pair in zip(l1,l2,l3)]
# print(average2)

# avearge3 = lambda pair
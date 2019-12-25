# advance min() and max()

numbers = [1,2,4,5,7]
print(max(numbers))
def func(item):
    return len(item)
names = ['jaymin','mehuls','sahal','mahendra']
print(max(names,key = lambda item:len(item)))

students = {
    'jaymin' :{'score':20,'age':24},
    'sahal': {'score':75,'age' :19},
    'mehul': {'score':76, 'age':23}
}
print(max(students,key=lambda item :students[item]['score']))


# students = [
#     {'name':'jaymin','score':90,'age':24},
#     {'name':'sahal','score':75,'age' :30},
#     {'name':'mehul','score':76, 'age':23}
# ]

# print(max(students,key=lambda item:item.get('age'))['name'])
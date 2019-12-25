# insert method 

fruits1 = ['mango' ,'orange']
#fruits1.insert(20,'grapes')
#print(fruits1)
fruits2 = ['grapes','apple']

fruits = fruits1 + fruits2 # join two list (concatenate)
print(fruits)

fruits1.extend(fruits2)
print(fruits1)
print(fruits2)

fruits1.append(fruits2)
print(fruits1)
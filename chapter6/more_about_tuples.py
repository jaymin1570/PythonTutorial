# looping in tuple 
# tuple with one elemrnt
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some function that tou can use with tuple

mixed = (1,2,3,4.0)

# for i in mixed:
#     print(i)

# print("\n")
# j=0
# while j<len(mixed):
#     print(mixed[j])
#     j+=1

# tuple wi
# th one element
# num = (1,)
# words = ('word1',)
# print(type(num))
# print(type(words))

# tuole without parenthesis
guitars = 'yamaha','baton rouge','taylor'
print(type(guitars))

# tuple unpacking
# num = ['jaymin','20']
# print(' '.join(num))

guitarists = ('maneli jaman','eddie van der meer','amdew foy')
guitarist1,guitarist2,guitarist3 = (guitarists)
print(guitarist1)

# list inside tuple
favorites = ('southern magnolia',['tokyo ghoul theme','landscape'])
# print(type(favorites))
favorites[1].pop()
favorites[1].append("we made it")
print(favorites)
print(type(favorites))

# function
# min ,max, sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))
# fromkeys
#d = {'name':'unknown','age':'unknown':}

# d = dict.fromkeys(['name','age'],['unknown','unknown'])
# print(d)
# d['name']= 'makwana'
# print(d)
# print(type(d))

# get method (useful)
d = {'name':'jaymin','age':'unknown'}
# print(d['names'])

print(d.get('name'))  # better

# if 'name' in d:
#     print('present')
# else:
#     print('not present')

if d.get('name'):
    print('present')
else:
    print('not present')

#  clear method

d1 = d.copy()
print(d1)
d.clear()
print(d)
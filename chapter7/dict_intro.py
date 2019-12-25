# what are dictionaries
# unorder collection of data in key : value pair

# how to create dictionary
user = {'name':'jaymin','age' :20}
# print(user)
# print(type(user))
print(user['name'])
print(user['age'])

# second method to create dictionary
user1 = dict(name ='jaymin',age = 20)
# print(user1)
# print(type(user1))

# which type of data a dictionary can store ?
# anything
# numbers, stirng, dictionary

user_info = {
    'name' : 'jaymin',
    'age' : '20',
    'fav_movie' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tale']
}
print(user_info['fav_movie'])

# users = {
#     'user1' : {
#         'name' : 'jaymin',
#     'age' : '20',
#     'fav_movie' : ['coco','kimi no na wa'],
#     'fav_tunes' : ['awakening','fairy tale']
#     },
#     'user2' : {

#     }
    
# }

# how to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'mohit'
user_info2['age'] = 20
print(user_info2)
print(user_info2["age"])
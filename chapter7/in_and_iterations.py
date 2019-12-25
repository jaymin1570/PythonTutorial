# in keyword and iteration in dictiory

user_info = {
    'name' : 'jaymin',
    'age' : 20,
    'fav_movie' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tale']
}

# check if key exist in dictionary
# if 'name' in user_info.keys():
#     print("present")
# else: 
#     print('not present')

# check if value exist in dictionary ----> values method
# if 20 in user_info.values():
#     print("present")
# else:
#     print('not present')

# loops in dictionary

for i in user_info.values():
    print(i)

# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))
# print('\n')
# loops in dictionary
# for i in user_info:
#     print(user_info[i])

# item method
# user_item = user_info.items()
# print(user_item)
# print(type(user_item))

# for  i,j in user_info.items():
#     print(f"key is :{i} and values is :{j}")
# store data from user
users = {}
name,age = input("enter your name and age :").split(',')
fav_movies= input("your favorite movies(separated by comma): ").split(',')
fav_songs = input("your favorite songs(separated by comma): ").split(',')
fav_movies =list(fav_movies)
fav_songs= list(fav_songs)
users['name']=name
users['age']=age
users['fav_movie']=fav_movies
users['fav_songs']=fav_songs
for key,value in users.items():
    print(f"{key}: {value}")

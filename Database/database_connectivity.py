import mysql.connector

conn = mysql.connector.connect(host='localhost', username='root', password='',database='new_database2')

my_cursor = conn.cursor()

# query = "CREATE DATABASE new_database2"
# query = "SHOW DATABASES"
# query = "CREATE TABLE student(name VARCHAR(255),age INT)"
query = "INSERT INTO student(name,age) VALUES (%s,%s)"

values = [
    ('jaymin',21),('nikhil',25),('mehul',33),('sahal',22),('ronak',23)
]  
query = "SELECT * FROM student"

my_cursor.execute(query)

# for row in my_cursor:
#     print(row)

print(my_cursor.fetchall())

# for database_name in my_cursor:
#     print(database_name)

# print(my_cursor.fetchall())

conn.commit()
conn.close()
# replace() method
# find() method

string = "she is beautiful and she is good dancer"
print(string.replace(" ", "_"))
print(string.replace("is","was",3))
print(string.find("is",1))

pos_1= string.find("is")
print(pos_1)
pos_2 = string.find("is",pos_1 + 1)
print(pos_2)
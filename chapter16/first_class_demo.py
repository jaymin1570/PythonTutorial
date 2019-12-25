# class
# init method (constructor)
class Person:
    def __init__(self, first_name,last_name,age):
        # instance variable
        print('init method / constructor get called')
        self.Person_first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person('jaymin','makwana',20)
p2=Person('mahendra','parmar',21)

print(p1.Person_first_name)
print(p2.Person_first_name)
print(type(p1))
print(type(p2))

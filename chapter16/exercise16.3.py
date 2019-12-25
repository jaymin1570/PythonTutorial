
class Person:
    count_instance=0
    def __init__(self, first_name,last_name,age):
        Person.count_instance+=1
        # instance variable
        # print('init method / constructor get called')
        self.Person_first_name=first_name
        self.last_name=last_name
        self.age=age
# Person.count_instance=0
p1=Person('jaymin','makwana',20)
p2=Person('nikhil','khastiya',24)
# p2=Person()
# p3=Person()
print(Person.count_instance)

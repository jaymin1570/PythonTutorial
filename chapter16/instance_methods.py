# instance method 

l=[1,2,3,4]
l.pop()
print(l)

class Person:
    def __init__(self,first_name,last_name,age):
        print('a')
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def full_name(self):
        print('b')
        return f"{self.first_name} {self.last_name},your age is :{self.age}"
    def is_above_18(self):
        return self.age>18
            
p1=Person('jaymin','makwana',19)
print(p1.full_name())
# print(Person.full_name(p1))
print(p1.is_above_18())

l=[1,2,3]
# clear,pop
l.clear()
# list.clear(l)
print(l)

list.append(l,10)
# l.append(10)
print(l)
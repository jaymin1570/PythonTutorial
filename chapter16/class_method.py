# class method 
# different between class method and instance methodpython 

class Person:
    count_instance=0 # class variable / class attributes
    def __init__(self,first_name,last_name,age):
        print('a')
        Person.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    @classmethod 
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        print('b')
        return f"{self.first_name} {self.last_name},your age is :{self.age}"
    def is_above_18(self):
        return self.age>18
            
p1=Person('jaymin','makwana',19)
p2=Person('ronak','munjapara',21)
print(Person.count_instances())
print(Person.__name__)
print(type(p1))
# special magic method / dunder method 
# operator overloading
# polymorphism ----> method overriding

class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    
    def phone_name(self):
        return f"{self.brand} {self.model}"

    # str, repr
    def __str__(self):
        return f'{self.brand} {self.model} and price is: {self.price}'

    def __repr__(self):
        return f"Phone('{self.brand}' ,'{self.model}' ,{self.price})"

    def __len__(self):
        # return len(self.phone_name())
        return self.price

    def __add__(self,other):
        return self.price + other.price

class SmartPhone(Phone):
    def __init__(self,brand,model,price,camera):
        super().__init__(brand,model,price)
        self.camera=camera
    
    def phone_name(self):
        return f"{self.brand} {self.model} and price :{self.price} and camera:{self.camera}"

# l=[1,2,3]
# print(l)
# t=(1,2,3)
# print(len(t))
phone1=Phone('nokia','1100',1000)
phone2=Phone('nokia','1600',2000)
my_smartphone = SmartPhone('mi','redmi5a',7000,'16MP')
print(phone1.phone_name())
print(my_smartphone.phone_name())
print(len(my_smartphone))
# print(phone1 + phone2)
# print(len(phone1))
# print(str(phone1))
# print(repr(phone1))
# print(phone1)
# print(phone1.__repr__())
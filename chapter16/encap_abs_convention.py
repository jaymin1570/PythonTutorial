# encapsulation
# abstraction
# some special naming convention
# name mangling # __name


class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.__price=price

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass #twilio

phone1 =Phone('nokia','1100',1000)
print(phone1.full_name())
# print(phone1.__price)
print(phone1.__dict__)
print(phone1._Phone__price)
phone1._Phone__price=-1000
print(phone1._Phone__price)
# phone1._price = -1000
# print(phone1._price)

# _name # convention of private name
# __name__ # dunder / magic method

l=[3,4,1,2]
l.sort() # tim sort
print(l)
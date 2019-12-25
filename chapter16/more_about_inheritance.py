# multilevel inheritance
# method resolution order
# method overriding
# isinstance(), issubclass()

class Phone: # base class /parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)


    def full_name(self):
        return f"{self.brand} {self.model_name} "

    def make_a_call(self,number):
        return f"calling {number}......"

class Smartphone(Phone): # derived class / child
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        #two ways
        # Phone.__init__(self,brand,model_name,price) # uncommon way
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is :{self._price} "


class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is :{self._price} and ram:{self.ram} and internal memory {self.internal_memory} and rear camera:{self.rear_camera} and front camera :{self.front_camera}"

    

# phone1=Phone('Nokia','1100',1000)
Smartphone1=Smartphone('Mi','redmi5a',7000,'6GB','32GB','13MP')
FlagshipPhone1=FlagshipPhone('Mi','redmi5a',7000,'6GB','32GB','13MP','16MP')
# print(phone1.full_name())
# print(Smartphone1.full_name() + f"price is :{Smartphone1._price} and front camera:{Smartphone1.front_camera}")
# print(phone1.full_name())
# print(Smartphone1.full_name())
# print(FlagshipPhone1.full_name())
# print(help(FlagshipPhone))

#isinstance 
print(isinstance(Smartphone1,Phone))

#issubclass
print(issubclass(Smartphone,Phone))
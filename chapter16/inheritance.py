class Phone: # base class /parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)


    def full_name(self):
        return f"{self.brand} {self.model_name} {self._price}"

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
        return f"{self.brand} {self.model_name} {self._price}"

    def make_a_call(self,number):
        return f"calling {number}......"

phone1=Phone('Nokia','1100',1000)
Smartphone1=Smartphone('Mi','redmi5a',7000,'6GB','32GB','13MP')
print(phone1.full_name())
print(Smartphone1.full_name() + f"price is :{Smartphone1._price}")
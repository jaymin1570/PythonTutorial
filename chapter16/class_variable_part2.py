class Laptop:
    discount_percent =10
    def __init__(self,brand,model_name,price):
        self.Laptop_brand=brand
        self.Lpatop_model_name=model_name
        self.Laptop_price=price
        self.Laptop_name=brand +' '+model_name

    def apply_discount(self):
        discount=self.Laptop_price-((self.Laptop_price*self.discount_percent)/100)
        return f"after appling discount price:{discount}"

# Laptop.discount_percent=100
l1=Laptop('HP','HP 15-da007ttx',48000)
l2=Laptop('apple','macbook',230000)
print(l1.Laptop_name)
print(l1.Laptop_price)
print(l1.apply_discount())
print(l2.Laptop_name)
print(l2.Laptop_price)

l2.discount_percent=50

print(l2.__dict__)
print(l2.apply_discount())
print(l1.__dict__) 
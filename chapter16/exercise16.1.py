
class Laptop:
    def __init__(self,brand,model_name,price):
        self.Laptop_brand=brand
        self.Lpatop_model_name=model_name
        self.Laptop_price=price
        self.Laptop_name=brand +' '+model_name
l1=Laptop('HP','HP 15-da007ttx','48000')
print(l1.Laptop_brand)
print(l1.Lpatop_model_name)
print(l1.Laptop_price)
print(l1.Laptop_name)

class Mobile:
    def __init__(self,name):
        self.name=name

class MobileStore:
    def __init__(self):
        self.mobiles=[]

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mmobile should be object of mobille class')
oneplus =Mobile('one plus 6')
# print(oneplus.name)
samsung='samsung galaxy s8'
mobostore=MobileStore()
mobostore.add_mobile(oneplus)
mobo_phones=mobostore.mobiles
print(mobo_phones[0].name)
# print(help(MobileStore))
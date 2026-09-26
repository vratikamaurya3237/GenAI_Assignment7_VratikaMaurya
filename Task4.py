#Taking Product as the Parent class
class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.__price=price
        self.category=category

    def get_price(self):
        return self.__price


#Creating class Laptop(Product), overriding get_info()
class Laptop(Product):
    def get_info(self):
        print("Laptop -> Name:", self.name, "|Price:", self.get_price(), "|Category:", self.category)

#Creating class Laptop(Product), overriding get_info()
class Mobile(Product):
    def get_info(self):
        print("Mobile -> Name:", self.name, "|Price:", self.get_price(), "|Category:", self.category)


#Creating objects of Laptop and Mobile
laptop1=Laptop("HP Victus", 72000, "Electronics")
mobile1=Mobile("OnePlus Nord", 35000, "Electronics")

#Looping over the objects and calling get_info()
items=[laptop1,mobile1]
for item in items:
    item.get_info()
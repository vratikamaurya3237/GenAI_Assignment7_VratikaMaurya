#taking Product class with price as a private attribute
class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.__price=price
        self.category=category

    def get_price(self):
        return self.__price

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.__price)
        print("Category:", self.category)

    #1. __str__ method
    def __str__(self):
        return f"Product({self.name}, {self.__price},{self.category})"

    #2. Operator overriding (__add__)
    def __add__(self,other):
        return self.__price + other.__price

#Testing with two product
p1=Product("Laptop", 72000, "Electronics")
p2=Product("Smartphone", 32000, "Electronics")

print(p1)
print(p2)
print("Combined Price:", p1+p2)
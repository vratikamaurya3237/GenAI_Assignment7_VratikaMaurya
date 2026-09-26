#Creating a class Product with Attributes: name, price, category
class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    #Creating method that prints product details
    def get_info(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Category: ", self.category)

    #Method that returns discounted price
    def apply_discount(self, percent):
        discounted_price=self.price-(self.price*percent/100)
        return discounted_price


#Creating two objects and calling get_info()
p1=Product("Phone", 30000, "Electronics")
p2=Product("Mouse", 12000, "Accessories")

print(p1.get_info())
print(p2.get_info())

print("Discounted Price of Product 1 (10% off): ", p1.apply_discount(10))
#Modifying the Product class: Making price a private attribute
#Writing the same code as in Task1.py
class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.__price=price
        self.category=category

    def get_info(self):
        print("Name: ", self.name)
        print("Price: ", self.__price)
        print("Category: ", self.category)

    #Getter Method
    def get_price(self):
        return self.__price

    #Setter Method: updates only if new_price>0
    def set_price(self,new_price):
        if new_price>0:
            self.__price=new_price

#Creating and testing 
p1=Product("Phone", 30000, "Electronics")
print("Original Price: ", p1.get_price())

p1.set_price(40000)
print("Updated Price: ", p1.get_price())

p1.set_price(-100)
print("Price after Invalid Updare: ", p1.get_price())
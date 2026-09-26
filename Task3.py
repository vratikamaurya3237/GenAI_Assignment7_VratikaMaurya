#Using the parent class Product
class Product:
    def __init__(self, name, price, category):
        self.name=name
        self.__price=price
        self.category=category

    def get_price(self):
        return self.__price

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.__price)
        print("category:", self.category)


#Creating a subclass ElectronicProduct that inherits from Product
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name,price,category)
        self.warranty_years=warranty_years

    #Overriding the get_info() tp include warranty info
    def get_info(self):
        super().get_info()
        print("Warranty: ", self.warranty_years, "years")


#Creating an object 
electronic_product=ElectronicProduct("Mobile Phone", 45000, "Electronics", 2)
electronic_product.get_info()
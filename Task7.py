#taking Product as the Parent class
class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    def get_info(self):
        print("Name:", self.name, "| Price:", self.price, "| Category:", self.category)

    #Operator overloading to combine prices of two products
    def __add__(self,other):
        return self.price + other.price

#class Inventory
class Inventory:
    def __init__(self):
        #Attribute: list to store product objects
        self.products=[]

    #Method: adds a product to the list
    def add_product(self, product):
        self.products.append(product)

    #Method:removes a product by name
    def remove_product(self, name):
        for product in self.products: 
            if product.name==name:
                self.products.remove(product)
                break

    #Method: sums prices of all products
    def get_total_value(self):
        total=0
        for product in self.products:
            total=total+product.price
        return total

    #Method: prints info for each product
    def show_all_products(self):
        for product in self.products:
            product.get_info()

#Class Store
class Store:
    def __init__(self, store_name):
        self.store_name=store_name
        #Attribute: an Inventory object
        self.inventory=Inventory()

    #Method: takes input and creates a Product object
    def add_new_product(self):
        name=input("Enter product name: ")
        price=float(input("Enter product price: "))
        category=input("Enter product category: ")
        new_product= Product(name,price,category)
        self.inventory.add_product(new_product)

    #Method: prices total items and total value
    def show_summary(self):
        print("Store Name: ", self.store_name)
        print("Total Items: ", len(self.inventory.products))
        print("Total Value: ", self.inventory.get_total_value())

#1. Creating a Store object
my_store=Store("Tech World")

#2. Adding 3 products
my_store.add_new_product()
my_store.add_new_product()
my_store.add_new_product()

#3. Showing summary
my_store.show_summary()

print()
print("All Products in Inventory:")
my_store.inventory.show_all_products()

#4. Using __add__ to combine prices of two products
product_list=my_store.inventory.products
combined_price=product_list[0] + product_list[1]
print()
print("Combined price of first two products:", combined_price)
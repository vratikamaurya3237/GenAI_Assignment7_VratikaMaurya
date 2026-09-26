#ASSIGNMENT 7(Object Oriented Programming [OOPs]): This assignment has 7 Tasks covering classes, objects, encapsulation, inheritance, polymorphism, abstraction, magic methods, and operator overloading.

##Task 1:
- Created a class 'Product' with attributes 'name', 'price', and 'category', set inside the constructor ('__init__').
- Created a method 'get_info()' that prints the product's name, price, and category.
- Created a method 'apply_discount(percent)' that calculates and returns 'discounted_price=self.price-(self.price*percent/100)'.
- Created two objects, 'p1' and 'p2', and called 'get_info()' on each using 'print(p1.get_info())' and 'print(p2.get_info())', then tested 'apply_discount(10)' on 'p1'.

This task made me understand that a class bundles related data ('name', 'price', 'category') and behavior (get_info()', 'apply_discount()') together, and '__init__' sets up each object's own copy of that data when it's created. Since 'get_info()' only contains 'print()' statements and has no 'return' statement, it returns 'None' be default-so wrapping it in 'print(p1.get_info())' first prints the product product details, and then also prints 'None' (the value 'get_info()' returned) right after. A method like 'apply_discount()' can calculate and 'return' a value instead of printing it, which is why it needed a separate 'print()' at the call site to display its result.



##Task 2:
- Modified the 'Product' class so that 'price' is stored as a private attribute, 'self.__price', instead of a public one.
- Kept 'get_info()' printing the product's details, now reading from 'self.__price'.
- Added a getter method 'get_price()' that returns 'self.__price', and a setter method 'set_price(new_price)' that only updates 'self.__price' if 'new_price>0'.
- Created an pbject 'p1', printed its original price, updated it to a valid value ('40000') using the setter and printed the result, then tried an invalid value ('-100') and printed the price again to confirm it stayed unchanged.

This task made me understand that prefixing an attribute with double underscoree makes it private, so it can no longer be accessed directly from outside the class; it needs a getter method instead. A setter method can enforce rules before allowing a change, which is why only updates when the condition is true, silently ignoring invalid values. Testing both a valid and an invalid call shows that the private attribute is properly protected from being set to an incorrect value.



##Task 3:
- Used the same 'Product' class structure (with 'name', private '__price', and 'category') as the parent class.
- Created a subclass 'ElectronicProduct' that inherits from 'Product', adding an extra attribute 'warrant_years' in its own '__init__', which calls 'super().__init__(name, price, category)'first to set up the inherited attributes.
- Overrode 'get_info()' inside 'ElectronicProduct' to call 'super().get_info()' (runningg the parent's version first) and then print hte warranty information.
- Created an object of 'ElectronicProduct' and called 'get_info()' to demonstrate both inheritance and overriding.

This task made me understand that 'super().__init__(...)' lets a subclass reuse the parent class's constructor to set up shared attribute, instead of repeating that code in the subclass. Overriding a method in a subclass (like 'get_info()') can still call the parent's original version with 'super().get_info()', so the subclass's version extends the parent's behavior instead of completely replacing it. A subclass automatically has access to everything the parent calss defines, plus whatever new attributes and methods it adds itself.



##Task 4:
- Used a 'Product' parent class with 'name', private '__price', 'category', and a 'get_price()' getter method.
- Created two subclasses, 'Laptop(Product)' and 'Mobile(Product)', each overriding 'get_info()' with its own print style and label ('"Laptop -> ..."' and '"Mobile -> ..."'), both reading the price through 'self.get_price()' since '__price' is private.
- Created one object of each class, put them together in a list called 'items', and used a 'for' loop to call 'get_info()' on each item.

This task made me understand that polymorphism means the same method call ('item.get_info()') behaves differently depending on the actual object's class, even though both 'Laptop' and "mobile' objects are stored and looped over in the same generic way. Because '__price' is private, subclasses can't access it directly as 'self.__price' (due to name mangling); they need to go through the inherited 'get_price()' method instead. A single 'for' loop can call the correct overridden version of 'get_info()' automatically for each object in the list, without needing to check the object's type first.



##Task 5:
- Imported 'ABC' and 'abstractmethod' from the 'abc' module.
- Created an abstract class 'Payment(ABC)' with an abstract method 'process_payment(amount)' that has no implementation (just 'pass').
- Created two subclasses, 'CreditCardPayment' and 'UPIPayment', each overriding 'process_payment()' with a simple 'print()' statement describing the payment being processed.
- Tested both classes by creating an object of each and calling 'process_payment()' with a sample amount ('15000' and '7000').

This task made me understand that making 'Payment' inherit fron 'ABC' and marking 'process_payment()' with '@abstractmethod' means 'Payment' itself can't be instantiated directly- only its subclasses, once they provide their own implementation of the abstract method. Abstraction here defines a common interface that every payment type must implement, while letting each subclass decide exactly how it processes the payment.



##Task 6:
- Used a 'Product' classs with 'name', private '__price', 'category', 'get_price(0', and 'get_info()'.
- Added a '__str__' method that returns a formatted string like 'Product(name, privce, category)' using an f-string.
- Added an '__add__' method that returns 'self.__price + other.__price', allowing two 'Product' objects to be added together with '+'.
- Created two product objects, 'p1' and 'p2', printed each one directly with 'print(p1)' and 'print(p2)' (which automatically uses '__str__'), and printed 'p1+p2' to show the combined price.

This task made me understand that defining '__str__' changes what 'print()' shows for an object - instead of a default momory_address style output, 'print(p1)' now shows the readable string built inside '__str__'. Defining '__add__' lets a custom class support the '+' operator, so 'p1+p2' calls '__add__' behind the scenes and returns whatever that method defines, here the sum of the two private prices. Even though '__price' is private, '__add__' can still access 'other.__price' because both 'self' and 'other' are instances of the same 'Product' class, so the private attribute is accessible from within the class's own methods.



##Task 7:
- Created a 'Product' class with public 'name', 'price', and 'category' attributes, a 'get_info()' method, and an '__add__' method that returns the combined price of two products.
- Created an 'Inventory' class with a 'products' list, and methods 'add_product(product)' to append a product, 'remove_product(name)' to find and remove a product by name, 'get_total_value()' to sum the prices of all products, and 'show_all_products()' to call 'get_info()' on every product.
- Creagted a 'store' class with  a 'store_name' and an 'inventory' (an 'Inventory' object), with a method 'add_new_product()' that takes input from the user to build a new 'Product' and adds it to the inventory, and 'show_summary()' that prints the store name, total items, and total value.
- Tested the system by creating a 'Store' object ("Tech World"), calling 'add_new_product()' three times to add three products, calling 'show_summary()', printing all products in the inventory, and using '__add__' to combine the prices of the first two products in the list.

This task made me understand that a class liks 'Store' can hold another class's object as one of its own attributes ('self.inventory=Inventory()'), letting the 'Store' delegate tasks like storing and totaling products to the 'Inventory' object instead of handling that logic itself. Looping through 'self.products' inside Inventory's methods ('remove_product', 'get_total_value', 'show_all_products') is a common pattern for working with every item currently stored in a list of objects. The '__add__' method defined on 'product' isn't limited to use inside the 'Product' class itself - it can be used anywhere two 'Product' objects are added together, including from within a completely different class like 'Store' or from the main test code.

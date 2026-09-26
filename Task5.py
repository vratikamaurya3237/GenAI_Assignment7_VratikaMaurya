from abc import ABC, abstractmethod

#Creating an abstract class Payment with abstract method process_payment(amount)
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

#Creating a subclass CreditCardPayment and overriding process_payment()
class CreditCardPayment(Payment):
    def process_payment(self,amount):
        print("Processing credit card payment of", amount)

#Creating subclass UPIPayment and overrriding process_payment()
class UPIPayment(Payment):
    def process_payment(self,amount):
        print("Processing UPI payment of", amount)


#Testing all classes
credit_payment=CreditCardPayment()
credit_payment.process_payment(15000)

upi_payment=UPIPayment()
upi_payment.process_payment(7000)
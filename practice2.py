""" 
Task#2:

A car rental agency wants to automate its rental operations with an object-oriented program. 
The system should have the following classes:

Car: Attributes include model, manufacturer, registration_number, and status (available or rented).
 It should have a method displayCarDetails() to show the car's details.

Customer: Attributes include name and customer_id. Methods include rentCar(car) to rent a car and returnCar(car)
 to return a rented car.

VIPCustomer (Subclass of Customer): Adds an attribute rental_limit to specify the max number of cars a 
VIP customer can rent simultaneously (e.g., 2). The rentCar(car) method should ensure the VIP customer 
does not exceed this limit.

RentalTransaction: Attributes include the car and customer involved. Methods include createRental() for renting
 and closeRental() for returning a car.

The system should ensure:

a) A VIPCustomer can rent up to 2 cars at once.

b) Cars can only be rented if they are available.

c) Upon returning a car, the status should be updated to "available."
"""
class Car:
   def __init__(self, model, manufacturer, reg_number):
       self.model = model
       self.manufacturer = manufacturer
       self.reg_number = reg_number
       self.status = 'available'
 
   def displayCarDetails(self):
       print(f"{self.manufacturer} {self.model} ({self.reg_number}) - {self.status}")
 
class Customer:
   def __init__(self, name, customer_id):
       self.name = name
       self.customer_id = customer_id
       self.rented_cars = []
 
   def rentCar(self, car):
       if car.status == 'available':
           car.status = 'rented'
           self.rented_cars.append(car)
           print(f"{self.name} rented {car.model}")
       else:
           print("Car not available")
 
   def returnCar(self, car):
       if car in self.rented_cars:
           car.status = 'available'
           self.rented_cars.remove(car)
           print(f"{self.name} returned {car.model}")
       else:
           print("This car was not rented by the customer")
 
class VIPCustomer(Customer):
   def __init__(self, name, customer_id):
       super().__init__(name, customer_id)
       self.rental_limit = 2
 
   def rentCar(self, car):
       if len(self.rented_cars) >= self.rental_limit:
           print("Rental limit reached")
       else:
           super().rentCar(car)
 
class RentalTransaction:
   def __init__(self, car, customer):
       self.car = car
       self.customer = customer
 
   def createRental(self):
       self.customer.rentCar(self.car)
 
   def closeRental(self):
       self.customer.returnCar(self.car)
 
# Demo
car1 = Car("Civic", "Honda", "REG210")
vip = VIPCustomer("Saad", 201)
trans = RentalTransaction(car1, vip)
trans.createRental()
car1.displayCarDetails()
trans.closeRental()
car1.displayCarDetails()

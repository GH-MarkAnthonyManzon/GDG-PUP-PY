
# Defining the class car
class Car:
    def __init__(self, make, model, year): # adding it's values / constructor
        self.make = make
        self.model = model
        self.year = year

    def describe(self): # Method to print out the car's description
        return f"This car is a {self.year} {self.make} {self.model}."

# Car's instance created
my_Car = Car("Honda", "Civic", 2018)

# To print out the description
print(my_Car.describe())
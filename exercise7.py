# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

class Car:

    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        car_age  = self.year - self.make
        return(car_age)

c1 = Car(2019, 2016,"Toyota")
c2 = Car(2019, 1985,"Celica")
c1.age()
c2.age()


print(c1.age())
print(c2.age())
print(Car(2019,1905,"BMW").age())
class Car:
    driver = 1
    color = 'white'
    body = 'metal'
    milage = 0
    def add_miles(self, miles):
        self.milage += miles

class PassengerCar(Car):
    wheels = 4
    passenger = 0
    def __init__(self,brand, milage):
        self.brand = brand
        self.milage = milage

    def add_passanger(self, passenger):
        self.passenger += passenger

    def __str__(self):
        return "{} driver; {} color; {} body; {} miles; {} wheels; {} passengers; {} branded;".format(self.driver, self.color, self.body,self.milage, self.wheels, self. passenger, self.brand)



class Truck(Car):
    wheels = 6
    load = 0

    def __init__(self, brand, milage, load):
        self.brand = brand
        self.milage = milage
        self.load = load

    def add_load(self, load):
        self.load += load

    def __str__(self):
        return "{} driver; {} color; {} body; {} miles; {} wheels; {} load; {} branded;".format(self.driver, self.color, self.body,self.milage, self.wheels, self. load, self.brand)

hyundai = PassengerCar('Hyundai', 20000)
hyundai.add_miles(30000)
hyundai.add_passanger(3)
print (hyundai)

kamaz = Truck('Kamaz', 20000, 30)
kamaz.add_miles(30000)
kamaz.add_load(3)
print (kamaz)
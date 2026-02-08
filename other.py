class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def addpassenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def printpassengersnames(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}.")


mila = Human("Mila")
oksana = Human("Oksana")
olexandr1 = Human("Olexandr")
olexandr2 = Human("Olexandr")
alina = Human("Alina")
max = Human("Max")
kyrylo = Human("Kyrylo")

car = Auto("Mercedes")

car.addpassenger(mila, oksana, olexandr1, olexandr2, alina, max, kyrylo)
car.printpassengersnames()
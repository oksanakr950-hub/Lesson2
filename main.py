import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def ToStudy(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def ToSleep(self):
        print("I will sleep")
        self.gladness += 3

    def ToChill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def IsAlive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally!")
            self.alive = False

    def EndOfDay(self):
        print(f"Gladness = {self.gladness}, Progress = {round(self.progress, 2)}")

    def Life(self, day):
        day = "Day " + str(day) + " of " + self.name + " file."
        print(day)

        life_cube = random.randint(1, 3)

        if life_cube == 1:
            self.ToStudy()
        elif life_cube == 2:
            self.ToSleep()
        elif life_cube == 3:
            self.ToChill()

        self.EndOfDay()
        self.IsAlive()


Ruby = Student("Ruby")
print(Ruby.name)
print("Ruby`s gladness: ", Ruby.gladness)
print("Ruby`s progress: ", Ruby.progress)
print("Is Ruby alive? ", Ruby.alive)

for day in range(365):
    if not Ruby.alive:
        break
    Ruby.Life(day)
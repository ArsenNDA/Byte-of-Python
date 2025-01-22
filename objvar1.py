class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Robot: {self.name}")
        Robot.population += 1

    def __del__(self):
        print(f"Robot: {self.name} is being destroyed!")

        if Robot.population > 0:
            Robot.population -= 1
        else:
            print("Robot: I'm the last one!")

    def say_hi(self):
        print(f"Robot: Hi. I'm {self.name}.")

    def how_many():
        print(f"Robot: I have {Robot.population} robots.")

    how_many = staticmethod(how_many)

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
del droid1
del droid2
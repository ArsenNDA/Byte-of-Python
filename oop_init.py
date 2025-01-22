class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, {self.name}")

p = Person("John", 36)

p.say_hello()
class Schoolmember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Created schoolmember: ", self.name)
    def tell(self):
        print("Name: ", self.name,  ", Age: ", self.age, sep="")

class Teacher(Schoolmember):
    def __init__(self, name, age, salary):
        Schoolmember.__init__(self, name, age)

class Student(Schoolmember):
    def __init__(self, name, age, marks):
        Schoolmember.__init__(self, name, age)
        self.marks = marks
        print("Created student: ", self.name)

    def tell(self):
        Schoolmember.tell(self)
        print("Marks: ", self.marks, sep="")

t = Teacher('Mrs. shreya', 40, 30000)
s = Student('Swaroop', 25, 75)

t.tell()
s.tell()

print()

members = [t, s]
for member in members:
    member.tell()


age = 25
name = "Arsen"

print("My name is {0} and I am {1} years old".format(name, age))

print("My name is {name} and I am {age} years old".format(name=name, age=age))

print("My name is {name} and I am {age} years old".format(**locals()))

print("My name is {name} and I am {age} years old".format(**globals()))

print("My name is {name} and I am {age} years old".format(name="Arsen", age=25))

print("My name is {name} and I am {age} years old".format(name="Arsen", age=25, city="New York"))

print("My name is {name} and I am {age} years old".format(name="Arsen", age=25, city="New York", country="USA"))

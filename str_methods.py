name = "John"
print(name.upper())

if name.startswith("J"):
    print("Yes, the name starts with 'J'.")

if "e" in name:
    print("Yes, it contains the string 'e'.")

if name.find("e") != -1:
    print("Yes, it contains the string 'e'.")

print(name.replace("John", "Mary"))

print(name.upper().replace("J", "M"))

print(name.lower())

print(name.title())

print(name.split())

print("-".join(name.split()))

print(name.strip())

print(name.rstrip())

print(name.lstrip())

print(name.capitalize())

print(name.swapcase())

print(name.count("n"))

print(name.index("n"))

print(name.find("n"))

print(name.rfind("n"))

print(name.isalnum())

print(name.isalpha())

print(name.isdigit())

print(name.islower())

print(name.isupper())

print(name.istitle())

print(name.isspace())

mylist = ["John", "Jane", "Jeremy"]
delimiter = "|"
print(delimiter.join(mylist))

print(help(str))
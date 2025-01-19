ab = {
    "Swaroop": "swaarop@gmail.com",
    "Larry": "larry@wall.org",
    "Matsumoto": "matsumoto@yahoo.co.jp",
    "Spammer": "spammer@example.com",
}

print("Address of Spammer is :", ab["Spammer"])

del ab["Spammer"]

print("\nIn Address book {0} Contact\n".format(len(ab)))

for name, address in ab.items():
    print("{0} ({1})".format(name, address))

ab["Guido"] = "guido@example.com"

if "Guido" in ab:
    print("\nGuido is in Address book")
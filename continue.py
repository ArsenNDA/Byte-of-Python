while True:
    s = input("Enter a something: ")
    if s == "quit":
        break
    if len(s) < 3:
        print("Too short")
        continue
    print("Too long")

    print("Length of the string is: ", len(s))
number = 23
guess = int(input("Enter an integer : "))

if guess == number:
    print("Congratulations, you guessed it.")
    print("But you do not win any prizes!")
elif guess < number:
    print("No, it is a little higher than that")
else:
    print("No, it is a little lower than that")
print("Done")
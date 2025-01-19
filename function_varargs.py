def total(a=5, *numbers, **phonebook):
    print("a ", a)
    for single_number in numbers:
        print(single_number)


    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(1,2, 3, 4, 5, 6, 7, 8, 9, 10, Jack=1, John=2, Inge=3, Arsen=4, Viki=5))

listone = [1, 2, 3, 4, 5]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total

print(powersum(2, 3, 4, 5))

print(powersum(2, 3, 4, 5, 6, 7, 8, 9))
def printMax(x,  y):
    '''Prints the maximum of two numbers.
    Two values must be entered'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

printMax(3, 5)
print(printMax.__doc__)
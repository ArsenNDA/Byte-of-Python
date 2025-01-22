class ShortInputException(Exception):

    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

try:
    text = input("Enter something: ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print("Why did you do an EOF on me?")
except ShortInputException as ex:
    print('ShortInputException: Long input required. At least {0} characters.'.format(ex.atleast))
else:
    print("No exception occurred.")

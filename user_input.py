def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def is_palindrome_v2(text):
    return text.lower() == reverse(text.lower())

def is_palindrome_v3(text):
    text = text.lower()
    text = text.split()
    text = ''.join(text)
    print(text)
    return text == reverse(text)

something = input("Enter something: ")

if is_palindrome_v3(something):
    print("It's a palindrome!")
else:
    print("It's not a palindrome")
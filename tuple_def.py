def get_error_details():
    return (404, "Not Found")

error_num, error_msg = get_error_details()
print(error_num)
print(error_msg)
print(type(error_num))
print(type(error_msg))

a, *b = 1, 2, 3, 4, 5, 6
print(a)
print(b)

a = 5
b = 10
a, b = b, a
print(a)
print(b)



print("Simple reference")

shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist just one variable with the same object
del shoplist[0]

print("shoplist is", shoplist)
print("mylist is", mylist)

print("Copy by making a full slice")
mylist = shoplist[:]
del mylist[0]

print("shoplist is", shoplist)
print("mylist is", mylist)
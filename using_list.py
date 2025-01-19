shop_list = ["apple", "mango", "carrot", "banana"]

print("I must to buy: ", shop_list, "items")

print("I must to buy: ", len(shop_list), "items")

print("Buy: ", end=' ')
for item in shop_list:
    print(item, end=' ')


print("Encore il faut acheter du riz: ")
shop_list.append("rice")
print("Now my shop list is: ", shop_list)

print("Now i can sort my list: ")
shop_list.sort()
print("Sorted shop list is: ", shop_list)

print("First item I must buy is: ", shop_list[0])
old_item = shop_list[0]
del shop_list[0]
print("New shop list is: ", shop_list)
print("I bought the: ", old_item)
print("My list now has: ", len(shop_list), "items")
# This is second exercise
# This is  a factor of a restaurant

restfactor = [{"Code" : 1, "Dish" : "French Fries", "Price" : 3.99},
              {"Code" : 2, "Dish" : "Jumbo Onion Ring", "Price" : 7.75},
              {"Code" : 3, "Dish" : "Fried Cheese Sticks", "Price" : 8.25},
              {"Code" : 4, "Dish" : "Fried Mushrooms", "Price" : 6.45},
              {"Code" : 5, "Dish" : "Sweet Potato Fries", "Price" : 7.75}]
orderlist = []

print("Hello dear client, Here is the best restaurant!")
print("This is the restaurant's menu:")

factlen = len(restfactor)

for x in range(0, factlen, 1):
    print(restfactor[x])

print("""You can ordered with enter each code of dishes in a order sequence. For example "123""")
myorder = input("Please, enter your order :")

myorderlen = len(myorder)
for x in range(0, myorderlen, 1):
    ordernum = int(myorder[x])
    orderlist.append(restfactor[x])

print("your order is: ")

totalprice = 0.0
orderlen = len(orderlist)
for x in range(0, orderlen, 1):
    print(orderlist[x])
    totalprice += orderlist[x]["Price"]

print("And your TOTALPAYMENT Is", totalprice)

# End of the exercise
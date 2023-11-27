# I made a list first
my_list = [1, 2, 3, 4, 12, 45, 65, 77, 8, 1, 2]

# i defined a empty set:
repeating_elements = set()

# here I use a for loop to find out repeating elements:
for x in my_list:
    if my_list.count(x) > 1:
        repeating_elements.add(x)
print("repeating_items", repeating_elements)


# exercise 2:

# I define a restaurants menu with a python dictionary:
menu = {
    'pizza': 10,
    'sushi': 8,
    'pasta': 15,
    'soft_drinks': 3,
    'french fries': 5
}
print(menu)
index = 1
for dish in menu:
    print(f'{index}. {dish}: {menu[dish]} euro')
    index += 1

# I define a  while loop to get customer order:
customer_order = {}
while True:
    order = input("enter a dish name or number:( enter 'finish' if you dont need somthing else ): ")
    if order.lower() == 'finish':
        break

    dish = menu.get(order)
    if dish:
        customer_order[order] = dish
        print(f"{order} added to your order. ")
    else:
        print("it's wrong choice! please enter a valid dish name or number. ")
# here I am going to calculate customer final price:
print('\n complete orders: ')
for dish, price in customer_order.items():
    print(f"{dish}: {price} euro")

total_price = sum(customer_order.values())
print(f"\n final price: {total_price} euro")




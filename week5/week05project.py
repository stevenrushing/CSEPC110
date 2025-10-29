# The additional creative part is I created a string containing items that have been deleted. Perhaps someone wants to keep a list of purchased items, stuff they might buy regularly but don't need this time. This would be a place for it. 

test_item_list = ["milk", "eggs", "bread"]
test_price_list = ["3.49", "2.99", "3.99"]

def disp_menu():
    print("""
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. View removed items
6. Quit
    """)

def add_item(cart_list, price_list):
    item = input("What item would you like to add? ")
    price = input(f"What is the price of {item}? ")
    cart_list.append(item)
    price_list.append(price)
    return cart_list, price_list

def disp_cart(cart_list, price_list):
    print("The contents of the shopping cart are: ")
    display = ""
    for i in range(len(cart_list)):
        display += f"{i+1}. {cart_list[i]}     ${price_list[i]}\n"
    print(display)

def rem_cart(cart_list, price_list, old_items):
    disp_cart(cart_list, price_list)
    print()
    choice = input("Which item would you like to remove? ")
    while not choice.isnumeric():
        choice = input(f"Please enter a number between 1 and {len(cart_list)}")
        while choice > len(cart_list):
            choice = input("Which item would you like to remove? ")
    choice = int(choice)
    old_items += f"{cart_list[choice -1]}     ${price_list[choice - 1]}\n"
    del cart_list[choice - 1]
    del price_list[choice - 1]

    return cart_list, price_list, old_items

def disp_total(price_list):
    total = 0
    for item in price_list:
        total += float(item)
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

def disp_old_items(old_items):
    print(old_items)

def prog_loop():
    cart_items = []
    cart_prices = []
    quit_program = "no"
    old_items = ""
    while quit_program == "no":
        choice = ""
        disp_menu()
        choice = input("Please enter an action: ")
        if choice == "1":
            cart = add_item(cart_items, cart_prices)
            cart_items = cart[0]
            cart_prices = cart[1]
        elif choice == "2":
            disp_cart(cart_items, cart_prices)
        elif choice == "3":
            cart = rem_cart(cart_items, cart_prices, old_items)
            cart_items = cart[0]
            cart_prices = cart[1]
            old_items = cart[2]
        elif choice == "4":
            disp_total(cart_prices)
        elif choice == "6":
            quit_program = "yes"
        elif choice == "5":
            disp_old_items(old_items)
        else:
            continue

prog_loop()
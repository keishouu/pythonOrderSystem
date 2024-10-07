menu = {
    1: {"itemName": "Milktea",
        "price": 75},
    2: {"itemName": "Burger",
        "price": 80},
    3: {"itemName": "Fries",
        "price": 50},
    4: {"itemName": "Fishball",
        "price": 30},
    5: {"itemName": "Hotdog Sandwich",
        "price": 100},
    'c': {"itemName": "to Confirm Order"},
    'n': {"itemName": "to End"}
}

all_orders = []

def displayMenu():
    print("Enter your Order:")
    for selection in menu:
        print(f"'{selection}' for {menu[selection]['itemName']}")
    print()

def displayOrders(current_order):
    print("\nYOUR ORDERS:")
    if all_orders:
        previous_orders_str = '\n'.join([f"{item} x {quantity}" for quantity, item, _ in all_orders])
        print(f"{previous_orders_str}")
    if current_order:
        current_orders_str = '\n'.join([f" {item} x {quantity}" for quantity, item, _ in current_order])
        print(f"{current_orders_str}")
    print()

def takeOrder():

    total = sum(quantity * price for quantity, _, price in all_orders)
    current_order = []

    while True:
        displayMenu()
        selection = input(" ")

        if selection.isdigit() and int(selection) in menu:
            item = menu[int(selection)]
            try:
                quantity = int(input(f"How many?\n"))
                if quantity > 0:
                    cost = item['price'] * quantity
                    total += cost

                    current_order.append((quantity, item['itemName'], item['price']))
                    displayOrders(current_order)
                else:
                    print("Please enter a valid quantity (greater than 0).\n")
            except ValueError:
                print("Invalid quantity. Please enter a number.\n")

        elif selection == 'c':
            if current_order:
                print(f"Your total order amount is: {total}")
                all_orders.extend(current_order)
                processPayment(total)
            else:
                print("You haven't ordered anything yet!")
            break

        elif selection == 'n':
            print("Order ended without confirmation.")
            break

        else:
            print("Invalid selection. Please choose a valid option.\n")

def processPayment(total):
    while True:
        try:
            amount_paid = float(input("Please enter cash amount: "))
            if amount_paid >= total:
                change = amount_paid - total
                print(f"Thank you for your Order! Your change is: {change}")
                break
            else:
                print(f"Insufficient cash! Please reset your order.\nYour order has been reset.\n")
                takeOrder()
                break
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")

takeOrder()

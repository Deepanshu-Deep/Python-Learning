def print_menu(menu):

    print("Menu:")
    for item, details in menu.items():

        print(f"{item.capitalize()}: ₹{details['price']:.2f} (Stock: {details['stock']})")

def place_order(menu):

    orders = {}

    while True:

        print_menu(menu)
        print("Enter 'done' to finish the order.")
        food_item = input("Enter the food item you want to order: ").strip().lower()

        if food_item == "done":
            break

        if food_item not in menu:
            print("Invalid food item. Please try again.")
            continue

        quantity = input("Enter the quantity: ")

        while not quantity.isdigit():

            print("Invalid input. Please enter a valid quantity.")
            quantity = input("Enter the quantity: ")

        quantity = int(quantity)

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        if quantity > menu[food_item]["stock"]:
            print("Sorry, we don't have enough stock for your order.")
            continue

        menu[food_item]["stock"] -= quantity
        orders[food_item] = orders.get(food_item, 0) + quantity

    return orders


def calculate_total_bill(orders, menu):

    total_bill = 0
    for item, quantity in orders.items():
        total_bill += menu[item]["price"] * quantity
    return total_bill


def manage_inventory(menu):

    while True:
        print("\n")
        print_menu(menu)
        print("Enter 'add' to add new items to the inventory.")
        print("Enter 'update' to update the price of an existing item.")
        print("Enter 'restock' to restock an existing item.")
        print("Enter 'exit' to go back to the main menu.")

        command = input("Enter your choice: ").strip().lower()

        if command == "add":
            item_name = input("Enter the name of the new item: ").strip().lower()
            if item_name in menu:
                print("Item already exists in the inventory.")
                continue

            price = float(input("Enter the price of the item: "))
            stock = int(input("Enter the initial stock quantity: "))
            menu[item_name] = {"price": price, "stock": stock}
            print(f"{item_name.capitalize()} has been added to the inventory.")

        elif command == "update":
            item_name = input("Enter the name of the item to update: ").strip().lower()
            if item_name not in menu:
                print("Item not found in the inventory.")
                continue

            new_price = float(input("Enter the new price of the item: "))
            menu[item_name]["price"] = new_price
            print(f"{item_name.capitalize()} price has been updated.")

        elif command == "restock":
            item_name = input("Enter the name of the item to restock: ").strip().lower()
            if item_name not in menu:
                print("Item not found in the inventory.")
                continue

            quantity = int(input("Enter the quantity to restock: "))
            menu[item_name]["stock"] += quantity
            print(f"{item_name.capitalize()} has been restocked.")

        elif command == "exit":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid command. Please try again.")


def main():
    # Initialize the food menu with item, price (in rupees), and stock
    menu = {
        "burger": {"price": 170.00, "stock": 10},
        "pizza": {"price": 250.00, "stock": 15},
        "fries": {"price": 140.00, "stock": 20},
        "soda": {"price": 35.00, "stock": 30},
    }

    print("Welcome to the Mumbai Munchies!")

    while True:

        print("\n")
        print("Enter 'order' to place an order.")
        print("Enter 'inventory' to manage the inventory.")
        print("Enter 'exit' to quit the application.")

        command = input("Enter your choice: ").strip().lower()

        if command == "order":
            user_orders = place_order(menu)
            total_bill = calculate_total_bill(user_orders, menu)
            print("\nOrder Summary:")
            for item, quantity in user_orders.items():
                print(f"{item.capitalize()}: {quantity} x ₹{menu[item]['price']:.2f} = ₹{menu[item]['price'] * quantity:.2f}")

            print(f"Total Bill: ₹{total_bill:.2f}")
        elif command == "inventory":
            manage_inventory(menu)
        elif command == "exit":
            print("Thank you for using the Mumbai Munchies. Come Again.. Bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
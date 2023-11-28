class InventoryItem:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def update_details(self, price=None, quantity=None, category=None, warranty=None):
        try:
            if price is not None:
                if not isinstance(price, float) or price <= 0:
                    raise ValueError("Price should be positive integer")
                else:
                    self.price = price

            if quantity is not None:
                if not isinstance(quantity, int) or quantity <= 0:
                    raise ValueError("Quantity should be positive integer")
                else:
                    self.quantity = quantity

            if category is not None:
                self.category = category

            if warranty is not None:
                self.warranty = warranty
        except ValueError as e:
            print(f"Error:{e}")

    def display(self):
        return f"Name: {self.name}, Price:{self.price}, Quantity:{self.quantity}, Category:{self.category}"


class Electronics(InventoryItem):
    def __init__(self, name, price, quantity, category, warranty):
        super().__init__(name, price, quantity, category)
        self.warranty = warranty

    def display(self):
        base_info = super().display()
        return f"{base_info}, Warranty: {self.warranty} months"


inventory = {}
categories = set()


def add_item():
    try:
        name = input("Enter the item name: ")
        price = float(input("Enter the price of item: "))
        quantity = int(input("Enter the quantity: "))
        category = input("Enter the item's category: ")

        if price <= 0 or quantity <= 0:
            print("Price and quantity can't be zero.")
            return

        inventory[name] = InventoryItem(name, price, quantity, category)
        categories.add(category)
    except ValueError:
        print("Enter a valid numbers for price and quantity")


def add_electronics():
    try:
        name = input("Enter the item name: ")
        price = float(input("Enter the price of item: "))
        quantity = int(input("Enter the quantity: "))
        category = input("Enter the item's category: ")
        warranty = int(input("Enter the warranty months: "))

        if price <= 0 or quantity <= 0:
            print("Price and quantity can't be zero.")
            return

        inventory[name] = Electronics(name, price, quantity, category, warranty)
        categories.add(category)
    except ValueError:
        print("Enter a valid numbers for price,quantity and warranty")


def remove_item():
    name = input("Enter the item's name to be removed: ")
    if name in inventory:
        del inventory[name]
    else:
        print(f"{name} not found.")


def update_item():
    name = input("Enter item name to update: ")
    if name in inventory:
        item = inventory[name]
        print("""What do you want to update?\n 1.Price\n 2.Quantity\n 3.Category""")
        if isinstance(item, Electronics):
            print("4.Warranty")
        choice = int(input("Enter your choice: "))
        try:
            match choice:
                case 1:
                    new_price = float(input("Enter new price: "))
                    item.update_details(price=new_price)
                case 2:
                    new_quantity = int(input("Enter new quantity: "))
                    item.update_details(quantity=new_quantity)
                case 3:
                    new_category = input("Enter new category: ")
                    item.update_details(category=new_category)
                case 4:
                    new_warranty = int(input("Enter new warranty months: "))
                    item.update_details(warranty=new_warranty)
        except ValueError:
            print("Enter number for choice")
    else:
        print(f"{name} not found.")


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        for i, item in enumerate(inventory.values(), 1):
            print(f"{i}. {item.display()}")


def low_stock():
    print(inventory.keys())
    low_stock_item = [item for item in inventory.values() if item.quantity < 10]
    for i, item in enumerate(low_stock_item, 1):
        print(f"{i}.{item.display()}")


def sort_inventory():
    print(
        "How do you want sort inventory?\n 1.Name\n 2.Price\n 3.Quantity\n 4.Category\n "
    )
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            sorted_inventory = sorted(inventory.values(), key=lambda x: x.name)
        case 2:
            sorted_inventory = sorted(inventory.values(), key=lambda x: x.price)
        case 3:
            sorted_inventory = sorted(inventory.values(), key=lambda x: x.quantity)
        case 4:
            sorted_inventory = sorted(inventory.values(), key=lambda x: x.category)
        case _:
            print("Invalid choice!")
            return
    for item in sorted_inventory:
        print(item.display())


print(
    "Options:\n 1.Add Item\n 2.Add Electronics\n 3.Remove Item\n 4.Update Item\n 5.View Inventory\n 6.Low Stock Report\n 7.Sort Inventory\n 8.Exit\n 9.Help"
)
while True:
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            add_item()
        case "2":
            add_electronics()
        case "3":
            remove_item()
        case "4":
            update_item()
        case "5":
            view_inventory()
        case "6":
            low_stock()
        case "7":
            sort_inventory()
        case "8":
            print("Exiting the program.......")
            break
        case "9":
            print(
                "Options:\n 1.Add Item\n 2.Remove Item\n 3.Update Item\n 4.View Inventory\n 5.Low Stock Report\n 6.Sort Inventory\n 7.Exit\n 8.Help"
            )
        case _:
            print("Invalid Command! ")

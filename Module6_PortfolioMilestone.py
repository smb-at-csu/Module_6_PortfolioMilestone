class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for i, item in enumerate(self.cart_items):
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    self.cart_items[i].item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    self.cart_items[i].item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    self.cart_items[i].item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        if self.cart_items:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}")
            print(f"Total: ${self.get_cost_of_cart():.2f}")
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        if self.cart_items:
            print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("ITEM DESCRIPTIONS")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")
        else:
            print("SHOPPING CART IS EMPTY")

def print_menu(cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

def get_item_to_purchase():
    print("ADD ITEM TO CART")
    item_name = input("Enter the item name:\n")
    item_description = input("Enter the item description:\n")
    item_price = float(input("Enter the item price:\n"))  # Get price as float
    item_quantity = int(input("Enter the item quantity:\n"))
    return ItemToPurchase(item_name, item_description, item_price, item_quantity)

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)

    my_cart = ShoppingCart(customer_name, current_date)

    while True:
        print_menu(my_cart)
        choice = input("Choose an option:\n")

        if choice == 'a':
            item = get_item_to_purchase()
            my_cart.add_item(item)
        elif choice == 'r':
            item_name = input("Enter name of item to remove:\n")
            my_cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            updated_item = ItemToPurchase(item_name, "", 0, new_quantity) 
            my_cart.modify_item(updated_item)
        elif choice == 'i':
            my_cart.print_descriptions()
        elif choice == 'o':
            my_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

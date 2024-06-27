class Product:
    def __init__(self,product,price,quantity) -> None:
        self.product = product
        self.price = price
        self.quantity = quantity
    def get_product(self):
        return f"Name : {self.product} | Price : {self.price} | Quantity : {self.quantity}"

class ShoppingCart:
    def __init__(self) -> None:
        self.items = []

    def add_item(self,product,price,quantity):
        self.items.append(Product(product,price,quantity))

    def remove_item(self,product):
        for item in self.items:
            if item.product.lower() == product.lower():
                self.items.remove(item)
                break

    def update_quantity(self,product,new_quantity):
        for item in self.items:
            if item.product.lower() == product.lower():
                item.quantity = new_quantity
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += (item.price * item.quantity)
        return total
    
    def display_cart(self):
        print("------------Cart--------------")
        for item in self.items:
            print(item.get_product())
        print("-------------------------------")
        print(f"Total Cost : {self.calculate_total()}")
        print("-------------------------------")

cart = ShoppingCart()
while True:
    print("\nOptions:")
    print("1. Add product to cart")
    print("2. Remove product from cart")
    print("3. Update product quantity")
    print("4. View cart")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        cart.add_item(name, price, quantity)
    elif choice == '2':
        name = input("Enter product name to remove: ")
        cart.remove_item(name)
    elif choice == '3':
        name = input("Enter product name to update: ")
        new_quantity = int(input("Enter new quantity: "))
        cart.update_quantity(name, new_quantity)
    elif choice == '4':
        cart.display_cart()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
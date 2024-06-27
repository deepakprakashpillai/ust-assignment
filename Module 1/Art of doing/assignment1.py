inventory = {}

def add_product(name, quantity, price):
    if name in inventory:
        print(f"'{name}' already in inventory.")
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
        print(f"'{name}' added to inventory.")

def update_quantity(name, new_quantity):
    if name in inventory:
        inventory[name]['quantity'] = new_quantity
        print(f"Quantity updated for '{name}'.")
    else:
        print(f"'{name}' not found")

def generate_invoice():
    total_cost = 0
    for name, details in inventory.items():
        item_total = details['quantity'] * details['price']
        total_cost += item_total
        print(f"{name}: Quantity - {details['quantity']}, Price - Rs.{details['price']}/-, Total - Rs.{item_total}/-")
    print(f"Total Cost: Rs.{total_cost}/-")

add_product("Laptop", 10, 1200)
add_product("Mouse", 50, 20)
add_product("Keyboard", 30, 50)

update_quantity("Mouse", 45)
update_quantity("Monitor", 20)

generate_invoice()

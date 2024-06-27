inventory = [
    {"name": "apple", "price": 1.25, "quantity": 10},
    {"name": "bread", "price": 2.50, "quantity": 5}
]

for product in inventory:
    print(f"Product: {product['name']}, Price: Rs.{product['price']}/-, Quantity: {product['quantity']}, Total Value: Rs.{product['price']*product['quantity']}/-")

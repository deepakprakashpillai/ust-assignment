
shopping_cart = ["apples", "bread", "milk"]

def add_item(item):
    shopping_cart.append(item)
    print(f"Added '{item}' to the shopping cart.")

def remove_item(item):
    if item in shopping_cart:
        shopping_cart.remove(item)
        print(f"Removed '{item}' from the shopping cart.")
    else:
        print(f"'{item}' not found in the shopping cart.")

def display_cart():
    if shopping_cart:
        print("Shopping Cart:")
        for item in shopping_cart:
            print(f"{item}")
    else:
        print("Shopping Cart is empty.")

add_item("orange juice")
remove_item("bread")
display_cart()

cart_items = tuple(shopping_cart)
print("Converted cart_items Tuple:", cart_items)

try:
    cart_items[0] = "eggs"
except TypeError as e:
    print(f"TypeError: {e}")

updated_cart = list(cart_items)
updated_cart[0] = "eggs"
print("Updated shopping cart:", updated_cart)

print("------------------------------------------------------------------------------------------------------------------------------------------------")

song_info = ["Bohemian Rhapsody", "Queen", 377]

title = song_info[0]
artist = song_info[1]
duration = song_info[2]

print(f"Title: {title}, Artist: {artist}, Duration: {duration}")

print("------------------------------------------------------------------------------------------------------------------------------------------------")

car_details = ("Toyota", "Camry", 2023)

print(f"Car Make: {car_details[0]}, Model: {car_details[1]}, Year: {car_details[2]}")

print("Iterating over car_details Tuple:")
for detail in car_details:
    print(detail)



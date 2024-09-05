def linear_search(products, keyword):
    return [product for product in products if keyword.lower() in product.lower()]

products = ["Laptop", "Smartphone", "Tablet", "Headphones"]

result = linear_search(products, "Laptop")
print(result)

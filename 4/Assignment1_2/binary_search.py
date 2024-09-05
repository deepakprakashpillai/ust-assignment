def binary_search_iterative(products, keyword):
    low, high = 0, len(products) - 1
    while low <= high:
        mid = (low + high) // 2
        if products[mid] == keyword:
            return mid
        elif products[mid] < keyword:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(products, keyword, low, high):
    if low <= high:
        mid = (low + high) // 2
        if products[mid] == keyword:
            return mid
        elif products[mid] < keyword:
            return binary_search_recursive(products, keyword, mid + 1, high)
        else:
            return binary_search_recursive(products, keyword, low, mid - 1)
    return -1


products = ["Laptop", "Smartphone", "Tablet", "Headphones"]

result = binary_search_iterative(products, "Laptop")
result2 = binary_search_recursive(products,"Laptop",0,len(products))
print(result,result2)

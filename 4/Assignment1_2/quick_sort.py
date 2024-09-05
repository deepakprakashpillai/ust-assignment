def quicksort(products):
    if len(products) <= 1:
        return products
    pivot = products[len(products) // 2]
    left = [x for x in products if x < pivot]
    middle = [x for x in products if x == pivot]
    right = [x for x in products if x > pivot]
    return quicksort(left) + middle + quicksort(right)

products = [2,5,1,3,4]
print(quicksort(products))
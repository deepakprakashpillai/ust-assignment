def insertion_sort(products):
    for i in range(1, len(products)):
        key = products[i]
        j = i - 1
        while j >= 0 and key < products[j]:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key
    return products


products = [2,5,1,3,4]
print(insertion_sort(products))
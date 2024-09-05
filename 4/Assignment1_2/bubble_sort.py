def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j] > products[j+1]:
                products[j], products[j+1] = products[j+1], products[j]
    return products

def selection_sort(products):
    n = len(products)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if products[j] < products[min_idx]:
                min_idx = j
        products[i], products[min_idx] = products[min_idx], products[i]
    return products

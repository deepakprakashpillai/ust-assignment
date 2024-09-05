def selection_sort(products):
    n = len(products)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if products[j] < products[min_idx]:
                min_idx = j
        products[i], products[min_idx] = products[min_idx], products[i]
    return products

products = [2,5,1,3,4]
print(selection_sort(products))

def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2
    left_half = merge_sort(products[:mid])
    right_half = merge_sort(products[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list

products = [2,5,1,3,4]
print(merge_sort(products))
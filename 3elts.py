def largest_product_of_three(arr):
    if len(arr) < 3:
        return None  # Not enough elements for the product

    arr.sort()
    max_product = max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])
    
    return max_product

arr = [10, 3, 5, 6, 20]

result = largest_product_of_three(arr)
print("The largest product of any three elements is:", result)

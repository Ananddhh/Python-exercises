def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

# Example array and target sum
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10

# Find and print pairs
pairs = find_pairs_with_sum(arr, target_sum)
print("Pairs with sum", target_sum, ":", pairs)

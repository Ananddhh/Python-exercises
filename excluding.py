# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Create a new set with all elements from both sets but exclude the common ones
exclusive_elements = set1.symmetric_difference(set2)

# Print the result
print("New set with exclusive elements:", exclusive_elements)

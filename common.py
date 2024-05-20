# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Check if the sets have any common elements
common_elements = set1.intersection(set2)

# Print the result
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements")

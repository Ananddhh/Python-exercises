# Define the original tuple
original_tuple = (1, 2, 3, 4, 5)

# Element to remove
element_to_remove = 3

# Create a new tuple without the element
modified_tuple = tuple(x for x in original_tuple if x != element_to_remove)

# Print the modified tuple
print("Modified tuple:", modified_tuple)

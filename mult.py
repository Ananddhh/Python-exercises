# Define a tuple with a variable length
variable_length_tuple = (1, 2, 3, 4, 5)

# Unpack the tuple into multiple variables
a, b, *c = variable_length_tuple

# Print the unpacked variables
print("a:", a)
print("b:", b)
print("c:", c)

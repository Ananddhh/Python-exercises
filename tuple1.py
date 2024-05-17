# Concatenating Two Tuples Element-wise

# Define two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenate the tuples element-wise
concatenated_tuple = tuple(map(lambda x, y: x + y, tuple1, tuple2))

# Print the concatenated tuple
print("Concatenated tuple:", concatenated_tuple)

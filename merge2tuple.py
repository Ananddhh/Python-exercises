# Define two tuples
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

# Merge the tuples and remove duplicates by converting to a set and back to a tuple
merged_tuple = tuple(set(tuple1 + tuple2))

# Print the merged tuple
print("Merged tuple without duplicates:", merged_tuple)

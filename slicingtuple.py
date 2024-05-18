# Define a tuple and the desired size for sub-tuples
original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
size = 3

# Slice the tuple into multiple sub-tuples
sub_tuples = [original_tuple[i:i + size] for i in range(0, len(original_tuple), size)]

# Print the resulting list of sub-tuples
print("Sub-tuples:", sub_tuples)

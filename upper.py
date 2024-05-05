input_string = input("Enter a string: ")
uppercase_count = 0
for char in input_string:
    if 'A' <= char <= 'Z':
        uppercase_count += 1
print("Number of uppercase letters in the string:", uppercase_count)

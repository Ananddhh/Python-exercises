input_string = input("Enter a string: ")
output_string = ''

for char in input_string:
    if char == 'a':
        output_string += 'e'
    else:
        output_string += char

print("String after replacing 'a' with 'e':", output_string)



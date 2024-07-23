# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)


# print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
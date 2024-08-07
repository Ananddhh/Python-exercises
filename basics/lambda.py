# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

# summarize argument a, b and c and return the result:


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# use that function definiion to make a function that always doubles the number you send in :

def my_func(n):
    return lambda a : a * n

mydoubler = my_func(2)

print(mydoubler(11))
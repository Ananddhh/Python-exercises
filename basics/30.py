# To specify that a function can have only positional arguments, add , / after the arguments:

# Example
def my_function(x, /):
  print(x)

my_function(3)

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

# Example
def my_function(x):
  print(x)

my_function(x = 3)
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

# to specify that a function can have only keyword arguments, add +, before the arguments:

# example

def my_function(*, x):
  print(x)

my_function(x = 3)

# any arguments before the / , are positional-only, and NY rgument after the *, are keyword-only:

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# recursion example:

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print (result)
  else:
    result = 0
  return result

print("\n\nRecursion example Results")
tri_recursion(6)
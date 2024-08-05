# In Python a function is defined using the def keyword:


def my_function():
  print("Hello from a function")


def my_function():
  print("Hello from a function")
# To call a function, use the function name followed by parenthesis:
my_function()

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")

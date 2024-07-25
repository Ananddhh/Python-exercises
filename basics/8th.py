# String Concatenation
# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = "My name is John, I am " + age
print(txt)


# Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)


# Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."

The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Print the answer of a function:

def myFunction() :
  return True

print(myFunction())

# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
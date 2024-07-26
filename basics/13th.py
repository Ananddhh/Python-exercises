fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# newlist = [expression for item in iterable if condition == True]

# Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]

# With no if statement:

newlist = [x for x in fruits]

# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

# Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

# Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

# Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]

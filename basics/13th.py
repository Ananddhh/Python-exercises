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

With no if statement:

newlist = [x for x in fruits]
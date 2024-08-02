x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.


a = 33
b = 200

if b > a:
  pass



a = 50
b = 10
if a > b:
 print("Hello World")


#  Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
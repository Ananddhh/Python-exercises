age = int(input("Enter the person's age: "))

# Determine the age category
if 0 <= age <= 12:
    category = "child"
elif 13 <= age <= 19:
    category = "teenager"
elif 20 <= age <= 59:
    category = "adult"
elif age >= 60:
    category = "senior"
else:
    category = "Invalid age"

# Print the age category
print(f"The person is a {category}.")

side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

# Check if the sides form a valid triangle
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    result = "Valid"
else:
    result = "Invalid"

# Print whether the triangle is valid or not
print(f"The triangle is {result}.")

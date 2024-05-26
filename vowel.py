char = input("Enter a character: ")

# Check if the character is a vowel, consonant, or neither
if char.lower() in 'aeiou':
    result = "vowel"
elif char.isalpha():
    result = "consonant"
else:
    result = "neither"

# Print the result
print(f"The character is a {result}.")

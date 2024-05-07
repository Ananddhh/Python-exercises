def is_palindrome(input_string):
    # Reverse the input string
    reversed_string = input_string[::-1]
    
    # Check if the original and reversed strings are equal
    if input_string == reversed_string:
        return True
    else:
        return False

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("Yes, the string is a palindrome.")
else:
    print("No, the string is not a palindrome.")

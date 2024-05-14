def is_balanced(parentheses):
    stack = []
    for char in parentheses:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            if (char == ')' and stack[-1] == '(') or \
               (char == '}' and stack[-1] == '{') or \
               (char == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
    return len(stack) == 0

# Example usage:
input_string = input("Enter a string containing parentheses: ")
if is_balanced(input_string):
    print("Yes, the parentheses are balanced.")
else:
    print("No, the parentheses are not balanced.")

def decimal_to_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

number = int(input("Enter a decimal number: "))
print("Binary representation:", decimal_to_binary(number))

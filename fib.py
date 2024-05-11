def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

num = int(input("Enter a number: "))
fib_sequence = generate_fibonacci(num)
print("Fibonacci sequence up to", num, ":", fib_sequence)

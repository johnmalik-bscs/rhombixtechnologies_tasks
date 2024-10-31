def fibonacci(n):
    fib_sequence = [0, 1]  # Starting values F(0) = 0 and F(1) = 1
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]  # Return only up to n terms

# Get number of terms from the user
num_terms = int(input("Enter the number of terms: "))
if num_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    print(fibonacci(num_terms))

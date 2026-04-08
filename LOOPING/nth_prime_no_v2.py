def is_prime(num):
    """Checks if a number is prime without using the math module."""
    if num < 2:
        return False
    # Check divisors from 2 up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    """Finds the nth prime number."""
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

# Example: Find the 10th prime number
n = int(input("Enter the number"))
print(f"The {n}th prime number is: {nth_prime(n)}")
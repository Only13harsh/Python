#program to generate prime no from 1-1000 in python
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Prime numbers from 1 to 1000:")
for number in range(1, 1001):
    if is_prime(number):
        print(number, end=" ")

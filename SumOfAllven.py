upper_limit = int(input("Enter the upper limit: "))
even_sum = 0

for num in range(1, upper_limit + 1):
    if num % 2 == 0:
        even_sum += num
print(f"The sum of even numbers from 1 to {upper_limit} is: {even_sum}")

# The Final Function to Check for Prime Numbers
def is_prime(number):
    if number > 1:
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                return False
        return True
    return False

# Finding All Prime Numbers Between 100 and 300
prime_numbers = []
for num in range(100, 999999):
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)
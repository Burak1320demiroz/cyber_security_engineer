def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_divisors(n):
    return [i for i in range(1, n//2 + 1) if n % i == 0] + [n]

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    divisors = find_divisors(number)
    print(f"{number} is not a prime number. Its divisors are: {divisors}")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
primes = prime_numbers_in_range(start, end)
print("Prime numbers in range:", ", ".join(map(str, primes)))

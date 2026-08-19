def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
 
def primes_up_to(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]
 
 
if __name__ == "__main__":
    limit = 50
    print(f"Primes up to {limit}: {primes_up_to(limit)}")
 
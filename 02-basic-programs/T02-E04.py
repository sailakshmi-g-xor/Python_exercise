def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def primes_up_to(limit):
    return [number for number in range(limit + 1) if is_prime(number)]


def main():
    numbers = [int(token) for token in input().split()]
    for number in numbers:
        if is_prime(number):
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")

    primes = primes_up_to(50)
    print(f"Primes up to 50: {primes}")
    print(f"Count: {len(primes)}")


if __name__ == "__main__":
    main()


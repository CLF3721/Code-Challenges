'''
Print the prime numbers within a given range.
Prime numbers are greater than 1 and have no positive divisors other than 1 and itself.
'''

def is_prime(start: int, end: int) -> None:
    for n in range(start, end+1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    print(f"the number {n} is not a prime")
                    break
            else:
                # If loop did not break, n is prime
                print(n)
        else:
            print(f"the number {n} is not a prime")

st = int(input())
en = int(input())

is_prime(st,en)
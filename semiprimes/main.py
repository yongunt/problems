from math import sqrt


def some_factors(n:int) -> list:
    if n <= 1: return [1]

    factors:list = []
    i:int = 2
    while n > 1:
        if (n%i) == 0:
            factors.append(i)
            n /= i
            i = 1
        i += 1

    return factors


def is_prime(n:int) -> bool:
    if n <= 1: return False
    for i in range(2, n):
        if (n%i) == 0: return False
    return True


def is_semiprime(n:int) -> bool:
    if is_prime(n): return False 

    factors:list = some_factors(n)
    if len(factors) > 2: return False

    for i in factors:
        if not is_prime(i): return False
    return True


def is_squared(n:int) -> bool: return some_factors(n).count(sqrt(n)) >= 2


def semiprimes(n:int) -> tuple:
    all_semiprimes:list = []
    not_squared_semiprimes:list = []

    for i in range(1, n):
        if is_semiprime(i):
            all_semiprimes.append(i)
            if not is_squared(i): not_squared_semiprimes.append(i)

    return (all_semiprimes, not_squared_semiprimes)


print(semiprimes(20))
print(semiprimes(157))
print(semiprimes(1))


'''
semiprimes(20) ➞ ([4, 6, 9, 10, 14, 15], [6, 10, 14, 15])

semiprimes(157) ➞ ([4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 121, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155], [6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155])

semiprimes(1), ([], [])
'''
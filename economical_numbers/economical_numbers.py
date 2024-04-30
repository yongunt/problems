def is_prime(n:int) -> bool:
    if n <= 1: return False
    if n == 2: return True
    for i in range(2, n):
        if n%i == 0: return False
    return True


def prime_factorization_lenght(n:int) -> list:
    ans = []
    CONST = n

    while n > 1:
        for i in range(2, CONST):
            if n%i == 0 and is_prime(i):
                n /= i
                ans.append(str(i))
                break

    check = []
    holder = ""

    for i in ans:
        if i not in check and ans.count(i) > 1:
            holder += str(ans.count(i))
            check.append(i)

    ans = set(ans)

    return len("".join(ans) + holder)


def is_economical(n:int) -> str:
    n_lenght = len(str(n))
    fac_lenght = prime_factorization_lenght(n)

    if n_lenght > fac_lenght: return "Frugal"
    elif n_lenght == fac_lenght: return "Equidigital"
    return "Wasteful"


print(is_economical(14))
print(is_economical(125))
print(is_economical(1024))
print(is_economical(30))


'''
is_economical(14) ➞ "Equidigital"
# The prime factorization of 14 (2 digits) is [2, 7] (2 digits)
# Exponents equal to 1 are not counted

is_economical(125) ➞ "Frugal"
# The prime factorization of 125 (3 digits) is [5^3] (2 digits)
# Notice how exponents greater than 1 are counted

is_economical(1024) ➞ "Frugal"
# The prime factorization of 1024 (4 digits) is [2^10] (3 digits)

is_economical(30) ➞ "Wasteful"
# The prime factorization of 30 (2 digits) is [2, 3, 5] (3 digits)
'''
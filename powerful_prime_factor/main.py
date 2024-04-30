def is_prime(n:int) -> bool:
    if n <= 1: return False
    for i in range(2, n):
        if n%i == 0: return False
    return True


def prime_factors(n:int) -> list:
    prime_factors:list = []
    x:int = 1

    while n != 1:
        x += 1
        
        if n%x == 0 and is_prime(x):
            n = n/x
            prime_factors.append(x)
            x = 1

    return prime_factors


def express_factors(n:int) -> str:
    factors:dict = {}
    ans:str = ""
    len_check:int = 0

    for i in prime_factors(n): factors[i] = prime_factors(n).count(i)

    for i in factors:
        len_check += 1

        if factors[i] > 1: ans += str(i) + "^" + str(factors[i])
        else: ans += str(i)

        if len_check != len(factors): ans += " x "

    return ans


print(express_factors(2))
print(express_factors(4))
print(express_factors(10))
print(express_factors(60))


'''
express_factors(2) ➞ "2"

express_factors(4) ➞ "2^2"

express_factors(10) ➞ "2 x 5"

express_factors(60) ➞ "2^2 x 3 x 5"
'''
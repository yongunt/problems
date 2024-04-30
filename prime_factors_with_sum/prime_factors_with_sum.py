def is_prime(n:int) -> bool:
    if n <= 1: return False
    if n == 2: return True

    for i in range(2, n):
        if n%i == 0: return False

    return True  


def prime_factors(n:int) -> list:
    if n <= 1: return [1]
    if n == 2: return [2]

    factors:list = []

    for i in range(2, n+1):
        if n%i == 0 and is_prime(i): factors.append(i)

    return factors


def sum_prime(lst:list) -> str:
    ans:str = ""
    all_factors:list = []
    holder:int = 0

    for i in lst: all_factors += prime_factors(i)

    all_factors = list(set(all_factors))
    
    for i in all_factors:
        holder = 0
        
        for j in lst:
            if j%i == 0: holder += j

        ans += '('+ str(i) + ' ' + str(holder) +')'
        
    return ans


print(sum_prime([12, 15]))
print(sum_prime([7, 13, 18, 23, 24]))
print(sum_prime([3, 5, 7, 9, 11, 13]))


'''
sum_prime([12, 15]) ➞ "(2 12)(3 27)(5 15)"
# 2 is a prime factor of 12 results (2 12).
# 3 is a prime factor of 12 and 15, add 15 + 12, results (3 27).
# 5 is a prime factor of 15 results (5 15).
# 7, 11 and 13 are prime numbers but not a factor of any of the number
# in the given list.

sum_prime([7, 13, 18, 23, 24]) ➞ "(2 42)(3 42)(7 7)(13 13)(23 23)"

sum_prime([3, 5, 7, 9, 11, 13]) ➞ "(3 12)(5 5)(7 7)(11 11)(13 13)"
'''
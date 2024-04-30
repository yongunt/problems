from math import sqrt


def is_prime(n:int) -> bool:
    if n <= 1: return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return False
    return True


def prime_numbers(limit:int) -> int:
    ans:int = 0
    for i in range(2, limit):
        if is_prime(i): ans += 1
    return ans


print(prime_numbers(10))
print(prime_numbers(20))
print(prime_numbers(30))


'''
prime_numbers(10) ➞ 4
# 2, 3, 5 and 7

prime_numbers(20) ➞ 8
# 2, 3, 5, 7, 11, 13, 17 and 19

prime_numbers(30) ➞ 10
# 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
'''
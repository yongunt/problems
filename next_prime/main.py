from math import sqrt

def is_prime(n:int) -> bool:
    if n <= 1: return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0: return False
    return True


def next_prime(n:int) -> int:
    if is_prime(n): return n
    while True:
        n += 1
        if is_prime(n): return n


print(next_prime(12))
print(next_prime(24))
print(next_prime(11))


'''
next_prime(12) ➞ 13

next_prime(24) ➞ 29

next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.
'''
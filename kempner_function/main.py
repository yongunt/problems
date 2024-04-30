from math import sqrt, factorial


def is_prime(n:int) -> bool:
    if n <= 1: return False
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0: return False
    return True


def kempner(n:int) -> int:
    if is_prime(n): return n
    
    ans:int = 1
    while True:
        if factorial(ans) % n == 0: return ans
        ans += 1


print(kempner(2))
print(kempner(5))
print(kempner(6))
print(kempner(10))
print(kempner(2))


'''
kempner(2) ➞ 2

kempner(5) ➞ 5

kempner(6) ➞ 3

kempner(10) ➞ 5

kempner(2) ➞ 2
'''
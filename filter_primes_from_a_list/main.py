def is_prime(n:int) -> bool:
    if n <= 1: return False
    for i in range(2, n):
        if n%i == 0: return False
    return True


def filter_primes(lst:list) -> list:
    ans:list = []
    for i in lst:
        if is_prime(i): ans.append(i)
    return ans


print(filter_primes([7, 9, 3, 9, 10, 11, 27]))
print(filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]))
print(filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]))


'''
filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]

filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]

filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]
'''
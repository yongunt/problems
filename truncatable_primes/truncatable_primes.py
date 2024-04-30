def is_prime(n:int) -> bool:
    if n <= 1: return False
    flag = True
    for i in range(2, n):
        if n%i == 0: flag = False
    return flag


def truncatable(n:int) -> str:
    n = str(n)
    if '0' in n: return False

    left = []
    left_check = True
    right = []
    right_check = True
    
    for i in range(len(n)): right.append(n[:i+1])
    for i in range(len(n)): left.append(n[-1][:i+1][-1])

    for i in left:
        if not is_prime(int(i)): left_check = False
    for i in right:
        if not is_prime(int(i)): right_check = False

    if left_check and right_check: return "both"
    elif right_check: return "right"
    elif left_check: return "left"
    else: return False
    

print(truncatable(9137))
print(truncatable(5939))
print(truncatable(317))
print(truncatable(5))
print(truncatable(139))
print(truncatable(103))


'''
truncatable(9137) ➞ "left"
# Because 9137, 137, 37 and 7 are all prime.

truncatable(5939) ➞ "right"
# Because 5939, 593, 59 and 5 are all prime.

truncatable(317) ➞ "both"
# Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.

truncatable(5) ➞ "both"
# The trivial case of single-digit primes is treated as truncatable from both directions.

truncatable(139) ➞ False
# 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.

truncatable(103) ➞ False
# Because it contains a 0 digit (even though 103 and 3 are primes).
'''
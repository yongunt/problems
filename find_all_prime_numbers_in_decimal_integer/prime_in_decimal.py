def is_prime(n:int) -> bool:
    if n <= 1: return False
    if n == 2: return True

    for i in range(2, n):
        if n%i == 0: return False

    return True


def extract_primes(n:int) -> list:
    n:str = str(n)
    ans:list = []
    holder:list = []

    for i in range(1, len(n)+1): holder.append(n[0:i])
    for i in range(1, len(n)+1): holder.append(n[::-1][0:i])
    for i in range(1, len(n)+1): holder.append(n[::-1][0:i][::-1])
    for i in n: holder.append(i)

    for i in holder:
        if '0' not in i and is_prime(int(i)):
            if n.count(i) != ans.count(i): ans.append(i)        

    ans = [int(i) for i in ans]

    return sorted(ans)


print(extract_primes(1))
print(extract_primes(7))
print(extract_primes(73))
print(extract_primes(103))
print(extract_primes(1313))


'''
extract_primes(1) ➞ []

extract_primes(7) ➞ [7]

extract_primes(73) ➞ [3, 7, 73]

extract_primes(103) ➞ [3]

extract_primes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]
'''
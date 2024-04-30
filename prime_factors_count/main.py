def is_prime(n:int) -> bool:
    if n <= 1: return False
    elif n == 2: return True

    for i in range(2, n):
        if n%i == 0: return False
    
    return True


def factorize(n:int) -> list:
    factors:list = []
    ans:list = []
    holder:dict = {}
    x:int = 1

    while n != 1:
        x += 1
        if n%x == 0 and is_prime(x):
            factors.append(x)
            n /= x
            x = 1

    for i in factors: holder[i] = factors.count(i)
    for i in holder.keys(): ans.append((i, holder[i]))

    return ans


print(factorize(4))
print(factorize(10))
print(factorize(60))


'''
factorize(4) ➞ [(2, 2)]

factorize(10) ➞ [(2, 1), (5, 1)]

factorize(60) ➞ [(2, 2), (3, 1), (5, 1)]
'''
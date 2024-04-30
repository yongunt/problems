def factorial(n:int) -> int:
    ans:int = 1
    for i in range(1, n+1): ans *= i
    return ans


def trailing_zeroes(n:int) -> int:
    reversed_factorial:str = str(factorial(n))[::-1]
    
    if reversed_factorial[0] != '0': return 0
    
    x:int = 0
    ans:int = 0

    while True:
        if reversed_factorial[x] == '0':
            ans += 1
            x += 1
        else:
            break

    return ans


print(trailing_zeroes(6))
print(trailing_zeroes(30))


'''
trailing_zeroes(6) ➞ 1
# factorial(6) = 720

trailing_zeroes(30) ➞ 7
# factorial(30) = 265252859812191058636308480000000
'''
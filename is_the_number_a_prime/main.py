def prime(n:int) -> bool:
    if n <= 1: return False
    
    for i in range(2, n):
        if n%i == 0: return False

    return True


print(prime(1))
print(prime(2))
print(prime(7))
print(prime(56963))
print(prime(5151512515524))


'''
prime(1) ➞ False

prime(2) ➞ True

prime(7) ➞ True

prime(56963) ➞ True

prime(5151512515524) ➞ False
'''
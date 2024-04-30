def is_prime(n:int) -> bool:
    for i in range(2, n):
        if n%i == 0: return False
    return True


count:int = 1
x:int = 3

while True:
    if is_prime(x): count += 1
    if count == 10001:
        print(x)
        break
    x += 1
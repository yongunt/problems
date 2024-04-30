def is_prime(n:int) -> bool:
    if n <= 1: return False
    for i in range(2, n):
        if n%i == 0: return False
    return True


def prime_factor_count(n:int) -> int:
    factors_count:int = 0
    for i in range(2, n):
        if n%i == 0 and is_prime(i): factors_count += 1
    return factors_count


x:int = 10
factor_limit:int = 4
holder:list = []
flag:bool = False


while True:
    x += 1
    
    holder.append(prime_factor_count(x))
    
    for i in range(-1, (-1*factor_limit)-1, -1):
        if holder[i] != factor_limit:
            flag = False
            break
        else: flag = True

    if flag:
        print(x-factor_limit+1)
        break
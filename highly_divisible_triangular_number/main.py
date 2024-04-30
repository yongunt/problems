def factor_count(n:int) -> int:
    count:int = 0

    for i in range(1, n):
        if n%i == 0: count += 1

    return count


x:int = 0
holder:int = 0
while True:
    x += 1
    print(x)
    holder += x 

    if factor_count(holder) >= 500:
        print(x, holder)
        break

# answer: 12375th number --> 76576500
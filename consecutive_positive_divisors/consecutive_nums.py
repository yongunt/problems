def count_of_divisors(n:int) -> int:
    ans:int = 0
    for i in range(1, n+1):
        if n%i == 0: ans += 1
    return ans


result:int = 0
for i in range(2, 10**7):
    print(i)
    if count_of_divisors(i) == count_of_divisors(i+1): result += 1


print(result)
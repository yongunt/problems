def divisors(n:int) -> list:
    holder:list = []
    for i in range(1, n+1):
        if n%i == 0: holder.append(i)
    return holder


def GCD(nums:list) -> int:
    all_divisors:list = []
    ans:int = 0

    for i in nums:
        all_divisors += divisors(i)

    for i in all_divisors:
        if all_divisors.count(i) == len(nums): ans = i

    return ans


print(GCD([10, 20, 40]))
print(GCD([1, 2, 3, 100]))
print(GCD([1024, 192, 2048, 512]))


'''
GCD([10, 20, 40]) ➞ 10

GCD([1, 2, 3, 100]) ➞ 1

GCD([1024, 192, 2048, 512]) ➞ 64
'''
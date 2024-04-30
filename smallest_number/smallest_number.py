def smallest(n:int) -> int:
    ans:int = 0
    flag:bool = True

    while flag:
        ans += 1

        for i in range(1, n+1):
            if ans % i != 0:
                flag = True
                break
            flag = False

    return ans


print(smallest(1))
print(smallest(5))
print(smallest(10))
print(smallest(20))


'''
smallest(1) ➞ 1

smallest(5) ➞ 60

smallest(10) ➞ 2520

smallest(20) ➞ 232792560
'''
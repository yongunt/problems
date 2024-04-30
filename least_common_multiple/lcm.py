def lcm(lst:list) -> int:
    n:int = 1
    flag:bool = True

    while flag:
        ans:int = max(lst) * n
        for i in lst:
            if ans % i != 0:
                flag = True
                break
            flag = False
        n += 1

    return ans


print(lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(lcm([5]))
print(lcm([5, 7, 11]))
print(lcm([5, 7, 11, 35, 55, 77]))


'''
lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520

lcm([5]) ➞ 5

lcm([5, 7, 11]) ➞ 385

lcm([5, 7, 11, 35, 55, 77]) ➞ 385
'''
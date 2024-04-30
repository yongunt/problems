def power_ranger(n:int, a:int, b:int) -> int:
    ans:int = 0
    for i in range(b + 1):
        if i**n >= a and i**n <= b: ans += 1
    return ans


print(power_ranger(2, 49, 65))
print(power_ranger(3, 1, 27))
print(power_ranger(10, 1, 5))
print(power_ranger(5, 31, 33))
print(power_ranger(4, 250, 1300))


'''
power_ranger(2, 49, 65) ➞ 2
# 2 squares (n^2) lie between 49 and 65, 49 (7^2) and 64 (8^2)

power_ranger(3, 1, 27) ➞ 3
# 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)

power_ranger(10, 1, 5) ➞ 1
# 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)

power_ranger(5, 31, 33) ➞ 1

power_ranger(4, 250, 1300) ➞ 3
'''
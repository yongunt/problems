def bonus(day:int) -> int:
    ans:int = 0
    for i in range(1, day+1):
        if i >= 33 and i <= 40: ans += 325
        elif i >= 41 and i <= 48: ans += 550
        elif i > 48: ans += 600
    return ans


print(bonus(15))
print(bonus(37))
print(bonus(50))


'''
bonus(15) ➞ 0

bonus(37) ➞ 1625

bonus(50) ➞ 8200
'''
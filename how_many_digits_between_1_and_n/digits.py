def digits(n:int) -> int:
    ans:int = 0

    for i in range(1, n): ans += len(str(i))

    return ans


print(digits(1))
print(digits(10))
print(digits(100))
print(digits(2020))


'''
digits(1) ➞ 0

digits(10) ➞ 9

digits(100) ➞ 189

digits(2020) ➞ 6969
'''
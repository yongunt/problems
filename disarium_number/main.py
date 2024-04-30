def is_disarium(n:int) -> bool:
    n_str:str = str(n)
    total:int = 0

    for i in range(1, len(n_str)+1): total += (int(n_str[i-1])**i)

    if total == n: return True
    else: return False


print(is_disarium(75))
print(is_disarium(135))
print(is_disarium(544))
print(is_disarium(518))
print(is_disarium(466))
print(is_disarium(8))


'''
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True
'''
def is_polydivisible(n:int) -> bool:
    n:str = str(n)
    for i in range(1, len(n)+1):
        if int(n[:i]) % i != 0: return False
    return True

    
print(is_polydivisible(1232))
print(is_polydivisible(123220))


'''
is_polydivisible(1232) ➞ True
# 1     / 1 = 1
# 12    / 2 = 6
# 123   / 3 = 41
# 1232  / 4 = 308

is_polydivisible(123220 ) ➞ False
# 1   / 1 = 1
# 12   / 2 = 6
# 123   / 3 = 41
# 1232   / 4 = 308
# 12322   / 5 = 2464.4         # Not a Whole Number
# 123220   /6 = 220536.333...  # Not a Whole Number
'''
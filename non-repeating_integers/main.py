def is_num_in_base(num:int, base:int) -> bool:
    base_digits:list = [str(i) for i in range(base)]
    num:str = str(num)
    for d in num:
        if d not in base_digits: return False
    return True


def is_non_repeats(n:int) -> bool:
    n:str = str(n)
    for d in n:
        if n.count(d) > 1: return False
    return True


def non_repeats(base:int) -> int:
    max_num = int(str(base-1)*base)
    ans:int = 0
    for num in range(1, max_num):
        if is_num_in_base(num, base) and is_non_repeats(num): ans += 1
    return ans


print(non_repeats(2))
print(non_repeats(4))
print(non_repeats(5))
print(non_repeats(6))


'''
non_repeats(2) ➞ 2

non_repeats(4) ➞ 48

non_repeats(5) ➞ 260

non_repeats(6) ➞ 1630
'''
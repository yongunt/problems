def make_list(l:int) -> list: return [i for i in str(l)]


def rearranged_difference(n:int) -> int:
    n_small:int = int(''.join(sorted(make_list(n))))
    n_large:int = int(''.join(sorted(make_list(n)))[::-1])
    return n_large - n_small


print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))


'''
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
'''
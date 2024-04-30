def factor_count(n:int) -> int:
    if n <= 1: return 1

    ans:int = 0
    for i in range(1, n):
        if n%i == 0: ans += 1

    return ans


def factor_sort(nums:list) -> list:
    nums = sorted(nums)[::-1]
    highest_factor_count:int = 0
    current_num:int = 0 
    ans:list = []

    while nums != []:
        for num in nums:
            if factor_count(num) > highest_factor_count:
                current_num = num
                highest_factor_count = factor_count(num)

        highest_factor_count = 0

        nums.pop(nums.index(current_num))

        ans.append(current_num)

    return ans


print(factor_sort([9, 7, 13, 12]))
print(factor_sort([1, 2, 31, 4]))
print(factor_sort([5, 7, 9]))
print(factor_sort([15, 8, 2, 3]))


'''
factor_sort([9, 7, 13, 12]) ➞ [12, 9, 13, 7]

factor_sort([1, 2, 31, 4]) ➞ [4, 31, 2, 1]

factor_sort([5, 7, 9]) ➞ [9, 7, 5]

factor_sort([15, 8, 2, 3]) ➞ [15, 8, 3, 2]
'''
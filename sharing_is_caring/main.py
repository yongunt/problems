def show_the_love(nums:list) -> list:
    holder:int = 0
    
    for i in range(len(nums)):
        if nums[i] != min(nums):
            holder += nums[i] / 4
            nums[i] = nums[i] - (nums[i] / 4)

    nums[nums.index(min(nums))] = nums[nums.index(min(nums))] + holder

    for i in range(len(nums)):
        if nums[i] % 1 == 0: nums[i] = int(nums[i]) 

    return nums


print(show_the_love([4, 1, 4]))
print(show_the_love([16, 10, 8]))
print(show_the_love([2, 100]))


'''
show_the_love([4, 1, 4]) ➞ [3, 3, 3]

show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]

show_the_love([2, 100]) ➞ [27, 75]
'''
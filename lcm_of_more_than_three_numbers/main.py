def lcm_of_list(nums:list) -> int:
    counter:int = 1
    flag:bool = True

    while flag:
        holder:int = max(nums) * counter

        for i in nums:
            flag = False
            if (holder % i) != 0:
                flag = True
                break
        
        counter += 1

    return holder


print(lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(lcm_of_list([13, 6, 17, 18, 19, 20, 37]))
print(lcm_of_list([44, 64, 12, 17, 65]))


'''
lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 2520

lcm_of_list([13, 6, 17, 18, 19, 20, 37]) ➞ 27965340

lcm_of_list([44, 64, 12, 17, 65]) ➞ 2333760
'''
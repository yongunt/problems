def get_lucky_number(size:int, nth:int) -> int:
    main_list:list = [i for i in range(1, size+1)]
    eliminated:list = []
    survivors:list = [1]
    x:int = 1
    sieve:int = 2
    
    while sieve < len(main_list):
        for i in range((sieve-1), len(main_list), sieve): eliminated.append(main_list[i])

        main_list = [i for i in main_list if i not in eliminated]
        
        survivors.append(main_list[x])

        sieve = survivors[-1]

        x += 1

    return main_list[nth-1]
        

print(get_lucky_number(25, 5))
print(get_lucky_number(3, 2))
print(get_lucky_number(120, 13))


'''
get_lucky_number(25, 5) ➞ 13
# Same set and procedure as in example in above instructions.

get_lucky_number(3, 2) ➞ 3
# Original set = 1, 2, 3
# After first step = 1, 3
# No more steps possibles (filter is for every third element, length of set is 2)
# The second (nth) element is 3

get_lucky_number(120, 13) ➞ 49
# Same set as in animated gif in above instructions.
'''
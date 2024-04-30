def sum_of_factors(n:int) -> int:
    factors:list = []

    for i in range(1, n):
        if n%i == 0: factors.append(i)

    return sum(factors)


def is_abundent(n:int) -> bool:
    if n < sum_of_factors(n): return True
    else: return False


abundent_nums:list = []
sum_of_two_abundent_nums:list = []
non_sum_of_two_abundent_nums:list = [] 

for i in range(1, 28124):
    if is_abundent(i): abundent_nums.append(i)

for i in abundent_nums:
    for j in abundent_nums:
        if (i+j) > 28123: break
        sum_of_two_abundent_nums.append(i+j)

sum_of_two_abundent_nums:list = list(set(sum_of_two_abundent_nums)) 

for i in range(1, 28124):
    for j in sum_of_two_abundent_nums:
        if j > i:
            non_sum_of_two_abundent_nums.append(i)
            break
        elif i == j: break

print(sum(non_sum_of_two_abundent_nums))
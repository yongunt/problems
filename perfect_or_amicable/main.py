def sum_of_all_divisors(n:int) -> int:
    divisors:list = []

    for i in range(1, n):
        if n%i == 0: divisors.append(i)
    
    return sum(divisors)


def num_type(n:int) -> str:
    if sum_of_all_divisors(n) == n: return "Perfect"
    elif sum_of_all_divisors(sum_of_all_divisors(n)) == n: return "Amicable"
    else: return "Neither"


print(num_type(6))
print(num_type(2924))
print(num_type(5010))


'''
num_type(6) ➞ "Perfect"

num_type(2924) ➞ "Amicable"

num_type(5010) ➞ "Neither"
'''
def sum_of_factors(n:int) -> int:
    if n <= 2: return 0
    factors:list = []

    for i in range(1, n):
        if n%i == 0: factors.append(i)
    
    return sum(factors)


def amicable_numbers_sum(top_number:int) -> int:
    amicable_numbers:list = []

    for i in range(3, top_number):
        if i not in amicable_numbers and i != sum_of_factors(i):
            if i == sum_of_factors(sum_of_factors(i)):
                amicable_numbers.append(i)
                amicable_numbers.append(sum_of_factors(i))

    return sum(set(amicable_numbers))

print(amicable_numbers_sum(10000))
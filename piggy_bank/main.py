def num_of_days(cost:int, savings:int, start:int) -> int:
    days:int = 0
    daily_increase:int = start

    while True:
        days += 1
        
        if days % 7 == 0:
            daily_increase = start + 1
            start += 1
        
        savings += daily_increase

        daily_increase += 1

        if savings >= cost: return days


print(num_of_days(2050, 1200, 10))
print(num_of_days(10000, 2500, 50))
print(num_of_days(500, 300, 50))


'''
num_of_days(2050, 1200, 10) ➞ 53
# 2050: cost of car, 1200: savings, 10: start amount
# After 53 days he can buy a car.

num_of_days(10000, 2500, 50) ➞ 123
# After 123 days he can buy a car.

num_of_days(500, 300, 50) ➞ 4
# After 4 days he can buy a car.
'''
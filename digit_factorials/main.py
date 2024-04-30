from math import factorial

def is_curious_number(num:int) -> bool:
    num:str = str(num)
    nums_digits_factorials_sum:int = 0

    for digit in num: nums_digits_factorials_sum += factorial(int(digit))

    return nums_digits_factorials_sum == int(num)


ans:int = 0
for num in range(3, 500000):
    if is_curious_number(num=num): ans += num
print(ans)
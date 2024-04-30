def is_result_negative(n1:int, n2:int) -> bool: return (n1*n2) < 0

def multiply(n1:int, n2:int) -> bool:
    big_num:int = None
    small_num:int = None
    ans:int = 0

    if abs(n1) > abs(n2):
        big_num = abs(n1)
        small_num = abs(n2)
    else:
        big_num = abs(n2)
        small_num = abs(n1)

    for times in range(small_num): ans += big_num

    if is_result_negative(n1, n2): return ans * (-1)
    else: return ans


print(multiply(10, 2))
print(multiply(-51, -4))
print(multiply(3, 9))
print(multiply(-21, 5))
print(multiply(1024, 7))
print(multiply(273, -6))


'''
multiply(10, 2) ➞ 20

multiply(-51, -4) ➞ 204

multiply(3, 9) ➞ 27

multiply(-21, 5) ➞ -105

multiply(1024, 7) ➞ 7168

multiply(273, -6) ➞ -1638
'''
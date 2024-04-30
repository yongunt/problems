def digits_count(n:int) -> int:
    if n <= 0: return 1
    
    check:str = '1'
    length:int = 1

    while True:
        check += '0'

        if n >= int(check): length += 1
        else: return length


print(digits_count(4666))
print(digits_count(544))
print(digits_count(121317))
print(digits_count(0))
print(digits_count(12345))
print(digits_count(1289396387328))


'''
digits_count(4666) ➞ 4

digits_count(544) ➞ 3

digits_count(121317) ➞ 6

digits_count(0) ➞ 1

digits_count(12345) ➞ 5

digits_count(1289396387328) ➞ 13
'''
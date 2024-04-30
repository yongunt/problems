def arithmetic_operation(operation:str) -> int:
    operation:list = operation.split(' ')

    if operation[1] == '+': return int(operation[0]) + int(operation[2])
    elif operation[1] == '-': return int(operation[0]) - int(operation[2])
    elif operation[1] == '//':
        if operation[2] == '0': return -1
        return int(operation[0]) / int(operation[2])
    elif operation[1] == '*': return int(operation[0]) * int(operation[2])


print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("12 - 12"))
print(arithmetic_operation("12 * 12"))
print(arithmetic_operation("12 // 0"))


'''
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
'''
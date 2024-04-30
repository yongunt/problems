def change_locks(cells:list) -> list:
    for i in range(len(cells)):
        if cells[i] == 0: cells[i] = 1
        else: cells[i] = 0
    return cells


def freed_prisoners(cells:list) -> int:
    if cells[0] == 0: return 0

    ans = 0

    for i in range(1, len(cells)):
        if cells[i] == 1:
            ans += 1
            cells = change_locks(cells)

    return ans


print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))
print(freed_prisoners([1, 1, 1]))
print(freed_prisoners([0, 0, 0]))
print(freed_prisoners([0, 1, 1, 1]))


'''
freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4

freed_prisoners([1, 1, 1]) ➞ 1

freed_prisoners([0, 0, 0]) ➞ 0

freed_prisoners([0, 1, 1, 1]) ➞ 0
'''
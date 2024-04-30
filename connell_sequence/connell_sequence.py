def connell_sequence(start, end, n):
    all_lines = [[1]]
    ans = []

    for i in range(2, end+1):
        if i%2 == 0: all_lines.append([j for j in range(all_lines[-1][-1] + 1, i**2 + 1) if j%2 == 0])
        else: all_lines.append([j for j in range(all_lines[-1][-1] + 1, i**2 + 1) if j%2 != 0])

    for i in all_lines[start - 1 : end + 1]: ans += i

    if n in ans: return ans.index(n)
    else: return "Not Found"


print(connell_sequence(1, 3, 4))
print(connell_sequence(2, 3, 4))
print(connell_sequence(4, 5, 22))


'''
connell_sequence(1, 3, 4) ➞ 2
# sequence = [1, 2, 4, 5, 7, 9]
# Number 4 is at index 2

connell_sequence(2, 3, 4) ➞ 1
# sequence = [2, 4, 5, 7, 9]
# Number 4 is at index 1

connell_sequence(4, 5, 22) ➞ "Not Found"
# sequence = [10, 12, 14, 16, 17, 19, 21, 23, 25]
# Number 22 is not in the sequence
'''
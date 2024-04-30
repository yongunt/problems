def factors(n:int) -> list:
    if n < 1: return [1]
    ans:list = []

    for i in range(2, n + 1):
        if n%i == 0: ans.append(i)

    return ans


def ecg_seq_index(n:int) -> list:
    answer:list = [1, 2]
    current:int = 0

    while len(answer) < n+1:
        current += 1
        if current not in answer:
            for factor in factors(answer[-1]):
                if factor in factors(current):
                    answer.append(current)
                    current = 0
                    break

    return answer[n]


print(ecg_seq_index(3))
print(ecg_seq_index(5))
print(ecg_seq_index(7))


'''
ecg_seq_index(3) ➞ 6

ecg_seq_index(5) ➞ 9

ecg_seq_index(7) ➞ 8
'''
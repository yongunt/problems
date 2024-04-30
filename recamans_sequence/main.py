ans:list = []

def get_new_number(seq:list, index:int) -> int:
    n_if:int = seq[index-1] - index
    n_else:int = seq[index-1] + index

    if n_if > 0 and n_if not in seq: return n_if
    else:
        if n_else in seq: ans.append(n_else)
        return n_else


def recaman(n:int) -> list:
    if n <= 0: return [0]
    elif n == 1: return [0, 1]
    
    a:list = [0, 1]
    counter:int = 1

    while len(a) < n:
        a.append(get_new_number(a, counter+1))
        counter += 1

    return ans


print(recaman(20))
print(recaman(100))


'''
recaman(20) ➞ "---> Recaman's sequence: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62]
---> Duplicates for n = 20: []"

recaman(100) ➞ "---> Recaman's sequence: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62, 42, 63, 41, 18, 42, 17, 43, 16, 44, 15, 45, 14, 46, 79, 113, 78, 114, 77, 39, 78, 38, 79, 37, 80, 36, 81, 35, 82, 34, 83, 33, 84, 32, 85, 31, 86, 30, 87, 29, 88, 28, 89, 27, 90, 26, 91, 157, 224, 156, 225, 155, 226, 154, 227, 153, 228, 152, 75, 153, 74, 154, 73, 155, 72, 156, 71, 157, 70, 158, 69, 159, 68, 160, 67, 161, 66, 162, 65, 163, 64]
---> Duplicates for n = 100: [42, 43, 78, 79, 153, 154, 155, 156, 157]"
'''
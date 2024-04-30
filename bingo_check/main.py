def diagonal_check(matrix:list) -> bool:
    flag:bool = True
    # Left to Right
    holder = matrix[0][0]
    for i in range(len(matrix)):
        if holder != matrix[i][i]:
            flag = False
            break
    if flag: return True
    # Right to Left
    n:int = 0
    holder = matrix[0][-1]
    flag = True
    for i in range(len(matrix)):
        if matrix[i][len(matrix)-n-1] != holder:
            flag = False
            break    
        n += 1

    return flag


def horizontal_check(matrix:list) -> bool:
    flag:bool = True
    for i in range(len(matrix)):
        holder = matrix[0][i]
        flag = True
        for j in range(len(matrix)):
            if matrix[j][i] != holder:
                flag = False
                break
        if flag: return True
    return False


def vertical_check(matrix:list) -> bool:
    flag:bool = True
    for i in range(len(matrix)):
        holder = matrix[i][0]
        flag = True
        for j in range(len(matrix)):
            if matrix[i][j] != holder:
                flag = False
                break
        if flag: return True
    return False


def bingo_check(matrix:list) -> bool:
    if diagonal_check(matrix): return True
    elif vertical_check(matrix): return True
    elif horizontal_check(matrix): return True
    else: return False


print(bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]))

print(bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]))

print(bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]))

print(bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]))


'''
bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]) ➞ True

bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]) ➞ True

bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]) ➞ True

bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]) ➞ False
'''
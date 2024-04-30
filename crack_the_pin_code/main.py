NUMPAD:list[int] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None]
]


def check_minus_indexes(x:list[list[int]]) -> list[list[int]]:
    counter:int = 0
    while counter < len(x):
        if x[counter][0] < 0 or x[counter][1] < 0:
            x.pop(counter)
            counter = -1
        counter += 1
    return x


def get_index(n:int) -> list[int]:
    if n == None: return None
    for i in range(4):
        for j in range(3):
            if NUMPAD[i][j] == n: return [i, j]  


def create_list(ind:list[int]) -> list[str]:
    ans:list[str] = []
    inds:list[list[int]] = [
        [ind[0], ind[1]+1],
        [ind[0], ind[1]-1],
        [ind[0]-1, ind[1]],
        [ind[0]+1, ind[1]],
        [ind[0], ind[1]]
    ]

    inds = check_minus_indexes(inds)

    n:int = 0
    while n < len(inds):
        try:
            if NUMPAD[inds[n][0]][inds[n][1]] != None:
                ans.append(str(NUMPAD[inds[n][0]][inds[n][1]]))
        except:
            inds.pop(n)
            n = -1
        n += 1

    return ans


def crack_pincode(digits:str) -> list:
    output:list = [""]
    for d in digits:
        temp:list = []
        for n in create_list(get_index(int(d))):
            for o in output:
                temp.append(o+n)
        output = temp
    return sorted(set(output))


print(crack_pincode("46"))
print(crack_pincode("0"))
print(crack_pincode("2"))
print(crack_pincode("007"))


'''
# Instead of the 4 it could also be 1, 5, or 7.
# Instead of the 6 it could also be 3, 5, or 9.

crack_pincode("46") ➞
["13","15","16","19","43","45","46","49","53","55","56","59","73","75","76","79"]

crack_pincode("0") ➞ ["0", "8"]

crack_pincode("2") ➞ ["1", "2", "3", "5"]

crack_pincode("007") ➞ ["004","007","008","084","087","088","804","807","808","884","887","888"]
'''
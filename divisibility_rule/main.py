REPETING:list = [1, 10, 9, 12, 3, 4]


def reversed_and_make_list(n:int) -> list: return [int(i) for i in str(n)[::-1]]


def build_consts(len_of_num:int):
    consts:list = []
    counter:int = 0
    while len(consts) != len_of_num:
        consts.append(REPETING[counter%6])
        counter += 1
    return consts


def divisibility_rule(n:int) -> int:
    n:list = reversed_and_make_list(n)
    consts:list = build_consts(len(n))
    holder:int = 0
    ans:int = 0

    while True:
        for i in range(len(n)): ans += (n[i]*consts[i])
        
        if ans != holder:
            holder = ans
            ans = 0
            n:list = reversed_and_make_list(holder)
            consts:list = build_consts(len(n))
        else:
            return ans
            

print(divisibility_rule(1234567))
print(divisibility_rule(8529))
print(divisibility_rule(85299258))


'''
divisibility_rule(1234567) ➞ 87

divisibility_rule(8529) ➞ 79

divisibility_rule(85299258) ➞ 31
'''
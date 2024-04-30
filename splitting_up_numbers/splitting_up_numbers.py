def num_split(n:int) -> list:
    holder = []
    flag = False

    if n < 0:
        flag = True
        n *= -1

    n = list(str(n))
    
    for i in range(len(n)): holder.append(n[i] + ('0' * (len(n) - (i + 1))))

    if flag:
        for i in range(len(holder)):
            if holder[i] != '0': holder[i] = int('-' + holder[i])
            else: holder[i] = int(holder[i])
    else:
        for i in range(len(holder)): holder[i] = int(holder[i])

    return holder


print(num_split(39))
print(num_split(-434))
print(num_split(100))
print(num_split(-100))


'''
num_split(39) ➞ [30, 9]

num_split(-434) ➞ [-400, -30, -4]

num_split(100) ➞ [100, 0, 0]
'''
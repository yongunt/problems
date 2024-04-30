def loves_me(n:int) -> str:
    ans:str = ""
    holder:list = ["Loves me not", "Loves me"]

    for i in range(1, n+1):
        if i == n: ans += holder[i%2].upper()     
        else: ans += holder[i%2] + ", "

    return ans


print(loves_me(3))
print(loves_me(6))
print(loves_me(1))


'''
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"
'''
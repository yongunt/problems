def sum_round(n:int) -> str:
    reversed_n:str = str(n)[::-1]
    ans:str = ""

    for i in range(len(reversed_n)):
        if reversed_n[i] != '0': ans += ((reversed_n[i] + ('0' * i)) + " ")

    return ans


print(sum_round(101))
print(sum_round(1234))
print(sum_round(54210))


'''
sum_round(101) ➞ "1 100"

sum_round(1234) ➞ "4 30 200 1000"

sum_round(54210) ➞ "10 200 4000 50000"
'''
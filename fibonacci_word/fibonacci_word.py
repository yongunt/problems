def fibo_word(n:int) -> str:
    if n <= 2: return "invalid"
    elif n == 3: return "b, a, ab"
    
    ans:str = "b, a, ab"

    for i in range(n-3):
        holder:list = ans.split(", ")
        ans += ", " + holder[-1] + holder[-2]

    return ans


print(fibo_word(1))
print(fibo_word(3))
print(fibo_word(7))


'''
fibo_word(1) ➞ "invalid"

fibo_word(3) ➞ "b, a, ab"

fibo_word(7) ➞ "b, a, ab, aba, abaab, abaababa, abaababaabaab"
'''
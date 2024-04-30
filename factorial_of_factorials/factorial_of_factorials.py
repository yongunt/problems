def factorial(n:int) -> int:
    ans:int = 1
    for i in range(2, n+1): ans *= i
    return ans 


def fact_of_fact(n:int) -> int:
    ans:int = 1
    for i in range(2, n+1): ans *= factorial(i)
    return ans


print(fact_of_fact(4))
print(fact_of_fact(5))
print(fact_of_fact(6))


'''
fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200
'''
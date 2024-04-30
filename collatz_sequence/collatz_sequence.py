def max_collatz(n:int) -> int:
    ans:int = 0
    
    while n > 1:
        if n > ans: ans = int(n)

        if n%2 == 0: n /= 2
        else: n = (n*3) + 1

    return ans


print(max_collatz(10))
print(max_collatz(32))
print(max_collatz(85))


'''
max_collatz(10) ➞ 16
# Collatz sequence: 10, 5, 16, 8, 4, 2, 1

max_collatz(32) ➞ 32
# Collatz sequence: 32, 16, 8, 4, 2, 1

max_collatz(85) ➞ 256
# Collatz sequence: 85, 256, 128, 64, 32, 16, 8, 4, 2, 1
'''
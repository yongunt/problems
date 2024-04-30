def fib_fast(n:int) -> int:
    if n <= 2: return 1
    
    seq:list = [1, 1]
    
    while True:
        if len(seq) == n: return seq[-1]
        seq.append(seq[-1] + seq[-2])
    

print(fib_fast(5))
print(fib_fast(10))
print(fib_fast(20))
print(fib_fast(50))


'''
fib_fast(5) ➞ 5

fib_fast(10) ➞ 55

fib_fast(20) ➞ 6765

fib_fast(50) ➞ 12586269025
'''
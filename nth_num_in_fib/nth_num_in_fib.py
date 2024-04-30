def nth_num_in_fib(n:int) -> int:
    if n == 0: return 0
    elif n == 1: return 1
    else: return nth_num_in_fib(n-1) + nth_num_in_fib(n-2)


print(nth_num_in_fib(2))
print(nth_num_in_fib(12))
print(nth_num_in_fib(27))


'''
nth_num_in_fib(2) --> 1

nth_num_in_fib(12) --> 144

nth_num_in_fib(27) --> 196418
'''
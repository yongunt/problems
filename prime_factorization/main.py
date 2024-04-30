def is_prime(n):
  flag = True

  for i in range(2, n):
    if n % i == 0: flag = False
  
  return flag


def prime_factors(n):
  x = 1
  ans = []

  while n > 1:
    x+=1

    if n%x == 0 and is_prime(x):
      n = n/x
      ans.append(x)
      x = 1

  return ans


print(prime_factors(20))
print(prime_factors(100))
print(prime_factors(8912234))


'''
prime_factors(20) ➞ [2, 2, 5]

prime_factors(100) ➞ [2, 2, 5, 5]

prime_factors(8912234) ➞ [2, 47, 94811]
'''
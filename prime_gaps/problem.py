def is_prime(n):
  flag = True

  for i in range(2, n):
    if n % i == 0: flag = False
  
  return flag


def prime_gaps(gap, start, end):
  holder = []
  
  for i in range(start, end+1):
    if is_prime(i): holder.append(i)

    if len(holder) >= 2:
      if holder[-1] - holder[-2] == gap: return [holder[-2], holder[-1]]

  return None


print(prime_gaps(2, 5, 7))
print(prime_gaps(2, 5, 5))
print(prime_gaps(4, 130, 200))
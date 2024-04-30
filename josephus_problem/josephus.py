def josephus(soldiers, order):
  order -= 1
  soldiers = [i for i in range(1, soldiers + 1)]
  n = order

  while len(soldiers) > 1:
    soldiers.pop(n)
    n = (n + order) % len(soldiers)
    print(n)

  return soldiers[0]


print(josephus(41, 3))
print(josephus(35, 11))
print(josephus(11, 1))
print(josephus(2, 2)) 
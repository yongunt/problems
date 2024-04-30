def colomb(n):
  if n == 0: return []
  if n == 1: return [1]
  if n == 2: return [1, 2]

  main_list = [1, 2]

  c = 0

  while True:
    for j in range(main_list[c]):
      main_list.append(c+1)

    if c == 1:
      del main_list[0]
      del main_list[0]
    
    if len(main_list) > n: break
    
    c+=1

  return main_list[:n]

print(colomb(1))   
print(colomb(8))
print(colomb(10))
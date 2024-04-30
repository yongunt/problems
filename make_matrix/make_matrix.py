def id_mtrx(num):
  mylist = []
  holder = []
  n = 0

  for i in range(abs(num)):
    for j in range(abs(num)):
      holder.append(0)
    
    if num < 0:
      n-=1
      holder[n] = 1
      mylist.append(holder)
      holder = []
    else:
      holder[n] = 1
      mylist.append(holder)
      holder = []
      n+=1

  for i in mylist:
    for j in i:
      print(j, end=" ")
    print("")
        

id_mtrx(-10)
answer:int = 0
bigest_len:int = 0
current_len:int = 0
holder:int = 0

for i in range(2, 1000000):
    holder = i

    while holder != 1:
        current_len += 1

        if holder%2 == 0: holder /= 2
        else: holder = (3*holder) + 1

    if current_len > bigest_len:
        bigest_len = current_len
        answer = i
    
    current_len = 0


print(answer)
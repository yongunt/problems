def find_digit_square(n:str) -> str: return str(sum([int(i)**2 for i in n]))

ans = 0

for i in range(1, (10**7) + 1):
    while True:
        if find_digit_square(str(i)) == "1": break
        elif find_digit_square(str(i)) == "89":
            ans += 1
            break
        else: i = find_digit_square(str(i))
        

print(ans)
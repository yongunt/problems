def is_bouncy(n:str) -> bool:
    for i in range(1, len(n)):
        if int(n[i-1]) > int(n[i]): return True
    return False 


x:int = 100
bouncy_numbers:int = 0 

while True:
    print(x)
    if is_bouncy(str(x)) and is_bouncy(str(x)[::-1]): bouncy_numbers += 1
    if x * (99/100) == bouncy_numbers:
        print(x)
        break
    x += 1

# answer: 1587000
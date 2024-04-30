from string import ascii_uppercase as ALP

with open("names.txt", mode='r') as data:
    all_names:list = data.read().split(',')
    all_names.sort()
    
ans:int = 0
holder:int = 0

for i in range(len(all_names)):
    for j in all_names[i]:
        if j.upper() in ALP: holder += (ALP.index(j.upper()) + 1)

    ans += ((i+1) * holder)
    
    holder = 0

print(ans)
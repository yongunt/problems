total = 0
ans = []

for num in range(2, 1000000):
    holder = str(num)

    for j in holder: total += int(j)**5

    if total == num: ans.append(num)

    total = 0

print(sum(ans))  
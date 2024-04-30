def self_powers(limit:int) -> str:
    total:int = 0
    for i in range(1, limit+1): total += (i**i)
    return str(total)


print(self_powers(1000)[::-1][:10][::-1])
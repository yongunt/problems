seq:list = [1, 1]

while True:
    if len(str(seq[-1])) >= 1000:
        print(seq.index(seq[-1]) + 1)
        break
    else: seq.append(seq[-1] + seq[-2])
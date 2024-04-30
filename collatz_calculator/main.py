def collatz(n:int) -> list:
    num_of_time:int = 0
    bigest_number:int = n

    while n != 1:
        if n % 2 == 0: n /= 2
        else: n = (n*3) + 1

        num_of_time += 1

        if n > bigest_number: bigest_number = int(n)

    return [num_of_time ,bigest_number]


print(collatz(17))
print(collatz(6))
print(collatz(21))


'''
collatz(17) ➞ [12, 52]
# Because 17  52  26  13  40  20  10  5  16  8  4  2  1
# takes 12 steps and 52 is the highest number reached.

collatz(6) ➞ [8, 16]

collatz(21) ➞ [7, 64]
'''
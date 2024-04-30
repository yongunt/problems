def gcd(n1:int, n2:int) -> int:
    '''
    Find Great Common Divisor
    '''

    if n1 < n2: small_number, big_number = abs(n1), abs(n2)
    else: small_number, big_number = abs(n2), abs(n1)

    limit = big_number

    while True:
        for x in range(limit):
            if small_number * (x+1) > big_number:
                holder = small_number
                small_number = big_number - (small_number * x)
                big_number = holder
                
                if small_number == 0: return big_number

                break

        
""" print(gcd(91, 287)) """ # output: 7


check = "p"

while True:
    if check.lower() == "q": break

    x1 = input("Enter first number: ")
    x2 = input("Enter second number: ")

    try:
        x1 = int(x1)
        x2 = int(x2)

        print("gcd -> ", gcd(x1, x2), "\n")
        check = input("If you wanna quit press 'q', otherwise press anything not being 'q'\n")
        print("")

    except:
        print("Please enter a valid number :)\n")
        check = input("If you wanna quit press 'q', otherwise press anything not being 'q'\n")
        print("")
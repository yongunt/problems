check = "p"

while True:
    print("")
    check = input("If you wanna quit press 'Q', otherwise press anything not being 'Q'\n")

    if check.lower() == "q": break

    while True:
        try:
            print("")
            func = input("Please provide your function (use x as a variable and don't forget parentheses; otherwise you'll get error)\n-> ")
            def f(x): return eval(func)
            x = f(0) + 2 
            break
        except: print("Please provide valid values")

    while True:
        try:
            print("")
            xu = float(input("Please provide xl -> "))
            xl = float(input("Please provide xu -> "))
            ep = float(input("Please provide ep -> "))
            dn_ep = ep + 1
            break
        
        except: print("Please provide valid values")

    if f(xl) * f(xu) < 0:
        while ep < dn_ep:
            x0 = (xu + xl) / 2

            if f(x0) * f(xl) < 0: xu = x0
            elif f(x0) * f(xu) < 0: xl = x0

            dn_ep = abs(xu - xl) / 2
        print(x0)

    elif f(xl) * f(xu) == 0:
        if f(xl) == 0 and f(xu) != 0: print("xl is the root")
        elif f(xu) == 0 and f(xl) != 0: print("xu is the root")
        else: print("Both values are root")

    else: print("There is no root beetwen those values")
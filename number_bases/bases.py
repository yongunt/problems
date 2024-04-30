def from_x_to_10(base, number):
    base = int(base)

    if base > 10:
        my_dict = {
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15
        }

        number = str(number)[::-1]
        output = 0

        for i in range(len(number)):
            try: output += int(number[i]) * base**i
            except: output += int(my_dict[number[i].upper()]) * base**i

        return output

    else:
        x = [str(i) for i in range(base)]
        for i in str(number):
            if i not in x:
                return "err"

        number = str(number)[::-1]
        output = 0

        for i in range(len(number)): output += int(number[i]) * base**i

        return output

###############################################################################

def from_10_to_x(base, number):
    base = int(base)
    number = int(number)

    if base > 10:
        my_dict = {
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
        }

        list_holder = []
        output = []

        while True:
            holder = int(number % base)
            list_holder.append(holder)
            number = (number - holder) / base
            if number == 0: break
        
        for i in list_holder:
            if i > 9:
                output.append(my_dict[i])
            else:    
                output.append(str(i))
                       

        return "".join(output[::-1])

    else:
        output = [] 
        
        while True:
            holder = int(number % base)
            output.append(holder)
            number = (number - holder) / base
            if number == 0: break

        output = [str(i) for i in output]
        
        return "".join(output[::-1])


""" print(from_x_to_10(2, 101011111)) """ # output: 351
""" print(from_x_to_10(8, 7016)) """ # output: 3598
""" print(from_x_to_10(16, "2AE0B")) """ # output: 175627
##############################################################
""" print(from_10_to_x(8, 12345)) """ # output: 30071
""" print(from_10_to_x(16, 177130)) """ # output: 2B3EA


user_chose = "p"

while True:
    user_chose = input("If you wanna convert 10 base to something press '1'\nIf you wanna something to convert 10 base press '2'\nIf you wanna quit press 'q'\n")
    
    if user_chose.lower() == "q": break

    if user_chose == "1":
        while True:
            try:
                print("")
                base = input("Please provide base you wanna convert to -> ")
                number = input("Please provide number you wanna convert -> ")

                if from_10_to_x(base=base, number=number) == "err": x = 1/0

                print("Result ->", from_10_to_x(base=base, number=number), "\n")
                
                break
            
            except: print("Please enter valid numbers")
    
    elif user_chose == "2":
        while True:
            try:
                print("")
                base = input("Please provide base you wanna convert from -> ")
                number = input("Please provide number you wanna convert -> ")

                if from_x_to_10(base=base, number=number) == "err": x = 1/0

                print("Converted succesfully:", from_x_to_10(base=base, number=number), "\n")
                
                break
            
            except: print("Please enter valid numbers")
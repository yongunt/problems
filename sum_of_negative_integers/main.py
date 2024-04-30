def negative_sum(seq:str) -> int:
    all_negatives:list = []
    holder:str = ""

    for i in range(len(seq)):
        if seq[i] == '-':
            for j in range(i+1, len(seq)):
                if seq[j].isdigit(): holder += seq[j]
                try: 
                    if not seq[j+1].isdigit():
                        all_negatives.append(int(holder))
                        holder = ""
                        break
                except IndexError:
                    all_negatives.append(int(holder))
                    holder = ""
                    break

    return sum(all_negatives) * -1


print(negative_sum("-12 13%14&-11"))
print(negative_sum("22 13%14&-11-22 13 12"))


'''
negative_sum("-12 13%14&-11") ➞ -23
# -12 + -11 = -23

negative_sum("22 13%14&-11-22 13 12") ➞ -33
# -11 + -22 = -33
'''